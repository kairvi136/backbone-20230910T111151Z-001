document.addEventListener('DOMContentLoaded', function () {
    const compressionForm = document.getElementById('compression-form');
    const resultsDiv = document.getElementById('results');

    compressionForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        
        const inputData = document.getElementById('data-input').value;

        try {
            const response = await fetch('/compress', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data: inputData }),
            });

            if (!response.ok) {
                throw new Error('Failed to compress data.');
            }

            const data = await response.json();

            // Display the compressed data
            resultsDiv.innerHTML = `
                <h2>Compressed Data:</h2>
                <pre>${data.compressed_data}</pre>
            `;

            // Send the compressed data for decompression
            const decompressionResponse = await fetch('/decompress', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ compressed_data: data.compressed_data }),
            });

            if (!decompressionResponse.ok) {
                throw new Error('Failed to decompress data.');
            }

            const decompressedData = await decompressionResponse.json();

            // Display the decompressed data
            resultsDiv.innerHTML += `
                <h2>Decompressed Data:</h2>
                <pre>${JSON.stringify(decompressedData.data, null, 2)}</pre>
            `;

        } catch (error) {
            console.error('Error:', error);
            resultsDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    });
});

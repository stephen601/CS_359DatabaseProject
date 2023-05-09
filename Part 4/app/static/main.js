const searchForm = document.querySelector('#search-form');
  const schedulerSystemSelect = document.querySelector('#scheduler-system-select');
  const searchResultsDiv = document.querySelector('#search-results');

  searchForm.addEventListener('submit', (event) => {
    event.preventDefault(); // prevent the default form submission
    const schedulerSystem = schedulerSystemSelect.value;
    const url = `/api/display`;
    const data = new URLSearchParams();
    data.append('schedulerSystem', schedulerSystem);
    fetch(url, { method: 'POST', body: data })
      .then(response => response.json())
      .then(data => {
        // Build an HTML table to display the search results
        let tableHtml = '<table>';
        tableHtml += '<thead><tr><th>Model No</th><th>Serial No</th><th>Scheduler System</th></tr></thead>';
        tableHtml += '<tbody>';
        data.forEach(row => {
          tableHtml += `<tr><td>${row.modelNo}</td><td>${row.serialNo}</td><td>${row.schedulerSystem}</td></tr>`;
        });
        tableHtml += '</tbody></table>';

        // Update the search results div with the table
        searchResultsDiv.innerHTML = tableHtml;
      })
      .catch(error => {
        console.error('Error fetching search results:', error);
        searchResultsDiv.innerHTML = '<p>Error fetching search results.</p>';
      });
  });
// this function executes our search via an AJAX call
function runSearch( patient ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    $('#results1').hide();

    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#hypermutant_analysis').serialize();

    $.ajax({
        url: './search_hypermutants.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform patient search! textStatus: (" + textStatus +
		") and errorThrown: (" + errorThrown + ")");
        }
    });
}

// this processes a passed JSON structure representing hypermutants and draws it
//  to the result tables
function processJSON( data ) { 
    if (data.full_matches) {

    //set the span for total sequences
    $('#total_seq').text( data.total_seq );

    //set the span for total hypermutants
    $('#total_hyper').text( data.total_hyper );        
    
    //this will be used to keep track of row identifiers
    var next_row_num = 1;
       
    //iterate over each match and add a row to the result tissue table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
 
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#first_table');
                
        // add the tissue column
        $('<td/>', { "text" : item.tissue } ).appendTo('#' + this_row_id);
           
        // add the number of samples column
        $('<td/>', { "text" : item.total_tissue } ).appendTo('#' + this_row_id);

	//add the number of hypermutants column
	$('<td/>', { "text" : item.count_hyper } ).appendTo('#' + this_row_id);
        
    });
         
    // iterate over each match and add a row to the result full table for each
    $.each( data.full_matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#second_table');

        // add the sequence_id column
        $('<td/>', { "text" : item.sequence_id } ).appendTo('#' + this_row_id);

        // add the tissue column
        $('<td/>', { "text" : item.tissue } ).appendTo('#' + this_row_id);

        //add the new_date column
        $('<td/>', { "text" : item.new_date } ).appendTo('#' + this_row_id);

    });

    // iterate over each hypermutant and add a row to the open reading frame table for each
    $.each( data.orf, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#fourth_table');

        // add the sequence_id column
        $('<td/>', { "text" : item.sequence_id } ).appendTo('#' + this_row_id);

        // add the average length column
        $('<td/>', { "text" : item.average } ).appendTo('#' + this_row_id);

        //add the max column
        $('<td/>', { "text" : item.max } ).appendTo('#' + this_row_id);

        // add the min column
        $('<td/>', { "text" : item.min } ).appendTo('#' + this_row_id);

        // add the number of ORFs column
        $('<td/>', { "text" : item.count } ).appendTo('#' + this_row_id);


    });

  
    $('#results').show();
    $('#results1').hide();

   } else {
    
    // set the span that gives total sequences 
    $('#total_seq1').text( data.total_seq );
   
    //set the span that gives total matches
    $('#matches').text(data.match_count);

    // set the span that gives total Hypermut sequences
    $('#total_mut').text( data.total_mut );

    //set the span that gives total Hyperfreq sequences
    $('#total_freq').text( data.total_freq );

    //set the span that gives the fisher p-value
    $('#fisher-pvalue').text(data.fisher_pvalue);

    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // iterate over each match and add a row to the compare table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#third_table');

        // add the sequence_id column
        $('<td/>', { "text" : item.sequence_id } ).appendTo('#' + this_row_id);

        // add the hypermut column
        $('<td/>', { "text" : item.mut_hyper } ).appendTo('#' + this_row_id);
        
        //add the hyperfreq column
        $('<td/>', { "text" : item.freq_hyper } ).appendTo('#' + this_row_id);

	//add the match column
        $('<td/>', { "text" : item.is_match } ).appendTo('#' + this_row_id);
            
    });

    $('#results1').show();
    $('#results').hide();
   }
}

// run javascript once the page is ready
$(document).ready( function() {
      
      $( "#autocomplete" ).autocomplete({
      source: function( request, response ) {
        $.ajax( {
          url: "./search_hypermutants.cgi",
          dataType: "json",
          data: {
            patient: request.term
          },
          success: function( data ) {
            response($.map( data.full_matches.slice(0,5), function(item){
                return{
                        value:item.coded_name
                }
           }));
          }
        });
      },
        minLength:1
    });
    
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });   
});     

import pandas as pd

house_file_path = "DataSets/melb_data.csv"

data = pd.read_csv(house_file_path)

print(data.describe())


<table style="width:100%">
  <tr>
    <th>Number Of Weeks</th>
  </tr>
  <tr>
    <td>How Many Weeks?</td>
    <td><select><option value="No_Refresh" selected="true">No_Refresh</option><option value="Full_Refresh">Full_Refresh</option><option value="Job_History_Refresh">Job_History_Refresh</option></select></td> 
  </tr>
</table>

if(Data_Refresh == 'Full_Refresh'){ 
return '<table style="width:100%"><tr><th>Number Of Weeks</th></tr><tr><td>How_Many_Weeks</td><td><select><option value="1" selected="true">1</option><option value="2">2</option><option value="3">3</option></select></td></tr></table>'
}



<td class="setting-main">
<div name="parameter">
	<input name="name" type="hidden" value="Run_Sunday_Batch">
	<select name="value">
		<option value="No" selected="true">No</option>
		<option value="Yes">Yes</option>
	</select>
</div></td>
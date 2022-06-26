<?php
$vote = $_REQUEST['vote'];

//get content of textfile
$filename = "poll_result.txt";
$content = file($filename);

//put content in array
$array = explode("||", $content[0]);
$yes = $array[0];
$no = $array[1];

if ($vote == 0)
  {
  $yes = $yes + 1;
  }
if ($vote == 1)
  {
  $no = $no + 1;
  }

//insert votes to txt file
$insertvote = $yes;
$fp = fopen($filename,"w");
fputs($fp,$insertvote);
fclose($fp);
?>    
<table>
<tr>
<td><div id="votesMsg">Total Votes  :</div></td>
<td><div id="votesCounter">
<?php echo($yes); ?></div>
</td>
</tr>
</table>
<input type="Button" class="voteButton" name="vote" value="Vote again !!!" onclick="getVote(this.value)" />
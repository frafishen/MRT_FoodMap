<template>
	<div class="page">
		<div>
			<img alt="warning" src="../assets/warning.png" class="pic">
		</div>
		<div class="form">
			<div >
			<label for="name">Person Accused:</label>
			<input type="text" name="name"><br>
			</div>
			<label for="reason">Reason:</label><br>
			<textarea name="reason" rows="7" cols="63"></textarea>
		</div>
		<button class="button-container1">Cancel</button>
      <button class="button-container2"  @click="submitForm" >Confirm</button>
	</div>
</template>

<script>
	export default{
		name:'WarningPage',
		data(){

		}
	}
	
</script>

<style scoped>
	.page{
		margin:0 auto;
		background-color: #F0F0F0;		
		width: 772px;
		height: 454px;
		border-radius:10px;

	}
	.pic{
		width: 85px;
		height: 75px;
		margin: 0 auto;
		margin-top: 20px;
	}
	.form{
	
		font-family: 'Inter';
		font-style: normal;
		font-weight: 500;
		font-size: 20px;
		margin-left: 30px;
		display: block;	
		text-align: left;
	}
	input,label,textarea{
		margin-top: 10px;
		font-size: 20px;	
	}
	.button-container1 {
  margin-right: 50px;
    margin-top: 20px;
    font-size: 20px;
  }
  .button-container2 {
  margin-left: 50px;
    margin-top: 20px;
    background-color: darkorange;
    font-size: 20px;
    border-radius: 5px;
  }

</style>
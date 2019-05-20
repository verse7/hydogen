<template>
  <div>
		<div class="card mr-4 bg-transparent text-dark" > 
			<img class="card-img img-fluid"
					:src="'https://api.opencaribbean.org/api/v1/media/download/' + resource.mainImage">
			<small class="mt-1 font-weight-bold">{{ resource.name }}</small>
		</div>
	</div>
</template>

<script>
  export default {
    name: "ResourceCard",
    props: ['resource'],
    methods: {
      selectResource: function(){
        console.log(this.resource.appId);
        // localStorage.setItem(this.type, JSON.stringify(this.resource));

        // console.log(JSON.parse(localStorage.getItem(this.type)));
        router.push({name:"details", params:{resource: this.resource}});
      }
    }
  }
</script>

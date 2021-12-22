<template>
  <div class="crumbs">
      <el-breadcrumb separator="/">
          <el-breadcrumb-item>
              <i class="el-icon-lx-cascades"></i> 关键词查询
          </el-breadcrumb-item>
      </el-breadcrumb>
  </div>
  
  <div class="container">
              <div class="handle-box">
                  <el-input v-model="input" placeholder="关键词" id="inputText" style="width: 30%;"></el-input>
				  <el-button type="primary" @click="adddata()" style="width: 15%;">查询</el-button>
              </div>
  			<el-card>
  				<span>关键词查询</span>
  			</el-card>
			<el-table
			    :data="tableData"
			    height="250"
			    border
			    style="width: 100%">
			    <el-table-column
			      prop="movieid"
			      label="电影ID"
			      width="180">
			    </el-table-column>
			    <el-table-column
			      prop="movie_title"
			      label="电影名字"
			      width="180">
			    </el-table-column>
			    <el-table-column
			      prop="url"
			      label="电影链接">
			    </el-table-column>
				<el-table-column
				  prop="picture"
				  label="电影图片">
				  <template #default="scope">
				      <el-image class="table-td-thumb" :src="scope.row.thumb" :preview-src-list="[scope.row.thumb]">
				      </el-image>
				  </template>
				</el-table-column>
			  </el-table>
              
	</div>
</template>


<script>
  export default {
    data() {
      return {
		tableData: [],
        value: ''
      }
    },
	methods: {
          adddata(){
			    var key_word = document.getElementById("inputText").value;
				var api = "/api/keyword/?key_word="+key_word;
                Axios.get(api).then(response => {
                    if (response.data) {
                        this.tableData = response.data.data;
                    }
        	});
          },
        }
  }
</script>

<style scoped>
	.table-td-thumb {
	    display: block;
	    margin: auto;
	    width: 50px;
	    height: 201px;
	}
</style>
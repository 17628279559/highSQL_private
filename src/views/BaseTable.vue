<template>
	<div class="crumbs">
		<el-breadcrumb separator="/">
			<el-breadcrumb-item>
				<i class="el-icon-lx-cascades"></i> 用户ID
			</el-breadcrumb-item>
		</el-breadcrumb>
	</div>

  
  <div class="container">
              <div class="handle-box">
                    <el-input v-model="input" placeholder="用户ID" id="inputText" style="width: 30%;"></el-input>
    				<el-button type="primary" @click="adddata()" style="width: 15%;">查询</el-button>
              </div>
			<el-card>
  				<span id="name_">用户ID查询结果</span>
			</el-card>
			<el-table
			    :data="tableData"
			    height="80%"
			    border
			    style="width: 100%">
			    <el-table-column
			      prop="movieid"
			      label="电影ID"
			      width="75">
			    </el-table-column>
				<el-table-column
				  prop="picture"
				  label="电影图片" 
				  width="135">
				  <template #default="scope">
				      <el-image class="pict" :src="scope.row.picture" :preview-src-list="[scope.row.picture]">
				      </el-image>
				  </template>
				</el-table-column>
			    <el-table-column
			      prop="title"
			      label="电影名字"
			      width="300" >
				  <template #default="scope">
					  <el-link :href="scope.row.url" target="_blank" underline="false">{{ scope.row.title }}</el-link>
				  </template>
			    </el-table-column>
				<el-table-column
				  prop="rating"
				  label="评分"
				  width="60">
				</el-table-column>
				<el-table-column
				  prop="timestamp"
				  label="评分时间"
				  width="160">
				</el-table-column>
				<el-table-column
				  prop="tagid"
				  label="标签id"
				  width="80">
				</el-table-column>
				<el-table-column
				  prop="tag_name"
				  label="标签名称">
				</el-table-column>
				<el-table-column
				  prop="relevance"
				  label="标签相关度">
				</el-table-column>
			  </el-table>
              
	</div>
</template>


<script>
import Axios from 'axios';

  export default {
	name: "idselect",
    data() {
      return {
		tableData: [],
		input: '',
      }
    },
	methods: {
          adddata(){
			    var userid = document.getElementById("inputText").value;
				var api = "/api/userid/?userid="+userid;
                Axios.get(api).then(response => {
                    if (response.data) {
                        this.tableData = response.data.data;
						var namee = document.getElementById("name_");
						namee.innerHTML = response.data.name + "看过的电影有" + response.data.data.length + "个"
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
	.pict{
		display: block;
	    margin: auto;
	    width: 135px;
	    height: 201px;
	}
</style>
<style>
	.el-table .cell {
    white-space: pre;
	}
</style>
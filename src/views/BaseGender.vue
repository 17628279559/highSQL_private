<template>
  <div class="crumbs">
      <el-breadcrumb separator="/">
          <el-breadcrumb-item>
              <i class="el-icon-lx-cascades"></i> 性别推荐
          </el-breadcrumb-item>
      </el-breadcrumb>
  </div>
  
  <div class="container">
              <div class="handle-box">
                  <el-select v-model="value" filterable placeholder="请选择" id="inputText" style="width: 30%;">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
					<el-button type="primary" @click="adddata()" style="width: 15%;">查询</el-button>
              </div>
  			<el-card>
  				<span id="name_">性别推荐</span>
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
				  prop="average_rating"
				  label="平均评分">
				</el-table-column>
				<el-table-column
				  prop="num_of_rating"
				  label="评分人数">
				</el-table-column>
			  </el-table>
              
	</div>
</template>


<script>
import Axios from 'axios';
  export default {
    data() {
      return {
        options: [{
          value: '选项1',
          label: 'Man'
        }, {
          value: '选项2',
          label: 'Female'
        }],
		tableData: [],
        value: ''
      }
    },
	methods: {
          adddata(){
			    var gender = document.getElementById("inputText").value;
				var api = "/api/gender/?gender="+gender;
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
		.pict{
		display: block;
	    margin: auto;
	    width: 135px;
	    height: 201px;
}
</style>
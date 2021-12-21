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
                  <el-input v-model="input" placeholder="关键词"></el-input>
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
		tableData: [{
		          date: '2016-05-03',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄',
				  picture: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg'
		        }, {
		          date: '2016-05-02',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄'
		        }, {
		          date: '2016-05-04',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄'
		        }, {
		          date: '2016-05-01',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄'
		        }, {
		          date: '2016-05-08',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄'
		        }, {
		          date: '2016-05-06',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄'
		        }, {
		          date: '2016-05-07',
		          name: '王小虎',
		          address: '上海市普陀区金沙江路 1518 弄'
		        }],
        value: ''
      }
    }
  }
</script>

<style scoped>
	.table-td-thumb {
	    display: block;
	    margin: auto;
	    width: 40px;
	    height: 40px;
	}
</style>
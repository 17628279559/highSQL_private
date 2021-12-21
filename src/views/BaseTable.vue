<template>
  <div class="crumbs">
      <el-breadcrumb separator="/">
          <el-breadcrumb-item>
              <i class="el-icon-lx-cascades"></i> 用户ID查询
          </el-breadcrumb-item>
      </el-breadcrumb>
  </div>
  
  <div class="container">
              <div class="handle-box">
                  <el-input v-model="input" placeholder="用户ID"></el-input>
              </div>
  			<el-card>
  				<span>用户ID查询结果</span>
  			</el-card>
			<el-table
			    :data="tableData"
			    height="250"
			    border
			    style="width: 100%">
			    <el-table-column
			      prop="movieid"
			      label="电影ID"
			      width="50">
			    </el-table-column>
			    <el-table-column
			      prop="movie_title"
			      label="电影名字"
			      width="180" >
				  <template #default="scope">
					  <el-link :href="scope.row.url" target="_blank" underline="false">{{ scope.row.movie_title }}</el-link>
				  </template>
				  
			    </el-table-column>
				<el-table-column
				  prop="rating"
				  label="用户评分"
				  width="80">
				</el-table-column>
				<el-table-column
				  prop="timestamp"
				  label="评分时间"
				  width="180">
				</el-table-column>
			    
				<el-table-column
				  prop="picture"
				  label="电影图片">
				  <template #default="scope">
				      <el-image class="table-td-thumb" :src="scope.row.picture" :preview-src-list="[scope.row.picture]">
				      </el-image>
				  </template>
				</el-table-column>
				<el-table-column
				  prop="tagid"
				  label="标签id">
				</el-table-column>
				<el-table-column
				  prop="relevance"
				  label="标签相关度">
				</el-table-column>
				<el-table-column
				  prop="relevance"
				  label="标签名称">
				</el-table-column>
			  </el-table>
              
	</div>
</template>


<script>
  export default {
    data() {
      return {
        options: [{
          value: '选项1',
          label: 'Adventure'
        }, {
          value: '选项2',
          label: 'Animation'
        }, {
          value: '选项3',
          label: 'Children'
        }, {
          value: '选项4',
          label: 'Comedy',
        }, {
          value: '选项5',
          label: 'Fantasy'
        }, {
          value: '选项6',
          label: 'Romance'
        }, {
          value: '选项7',
          label: 'Drama'
        }, {
          value: '选项8',
          label: 'Action'
        }, {
          value: '选项9',
          label: 'Crime'
        }, {
          value: '选项10',
          label: 'Thriller'
        }, {
          value: '选项11',
          label: 'Horror'
        }, {
          value: '选项12',
          label: 'Mystery'
        }, {
          value: '选项13',
          label: 'Sci-Fi'
        }, {
          value: '选项14',
          label: 'IMAX'
        }, {
          value: '选项15',
          label: 'Documentary'
        }, {
          value: '选项16',
          label: 'War'
        }, {
          value: '选项17',
          label: 'Musical'
        }, {
          value: '选项18',
          label: 'Western'
        }, {
          value: '选项19',
          label: 'Film-Noir'
        }],
		tableData: [{
		          tagid:'6',
				  movieid:'5',
				  timestamp: '2016-05-03',
		          rating: '3.5',
		          address: '上海市普陀区金沙江路 1518 弄',
				  url: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  picture: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  movie_title: 'absd'
		        }, {
		          tagid:'6',
				  movieid:'5',
				  timestamp: '2016-05-03',
		          rating: '3.5',
		          address: '上海市普陀区金沙江路 1518 弄',
				  url: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  picture: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  movie_title: 'absd'
		        }, {
		          tagid:'6',
				  movieid:'5',
				  timestamp: '2016-05-03',
		          rating: '3.5',
		          address: '上海市普陀区金沙江路 1518 弄',
				  url: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  picture: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  movie_title: 'absd'
		        }, {
		          tagid:'6',
				  movieid:'5',
				  timestamp: '2016-05-03',
		          rating: '3.5',
		          address: '上海市普陀区金沙江路 1518 弄',
				  url: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  picture: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  movie_title: 'absd'
		        }, {
		          tagid:'6',
				  movieid:'5',
				  timestamp: '2016-05-03',
		          rating: '3.5',
		          address: '上海市普陀区金沙江路 1518 弄',
				  url: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  picture: 'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2565956404.jpg',
				  movie_title: 'absd'
		        }],
		input: '',
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
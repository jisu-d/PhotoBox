<script>
  const designs = [
    [
      {
        imgRoute: '/frame/1.jpg'
      },
      {
        imgRoute: '/frame/2.jpg'
      }
    ],
    [
      {
        imgRoute: '/frame/1.jpg'
      },
      {
        imgRoute: '/frame/2.jpg'
      }
    ]
  ]
</script>

<style>
  img{
    width: 10%;
  }
</style>

<div>
  {#each designs as design}
    <div>
      {#each design as desig}
        <img src={desig.imgRoute} alt="">
      {/each}
    </div>
  {/each}
</div>
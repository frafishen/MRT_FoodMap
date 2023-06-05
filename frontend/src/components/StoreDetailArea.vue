<template>
  <div class="hero-overlay bg-white shadow-2xl rounded-2xl">
    <!-- ========== info component ========== -->
    <div class="p-6">
      <div class="p-4">
        <h3 class="text-3xl text-center font-semibold leading-7 text-primary">{{ 'Hot Pot Paradise' }}</h3>
      </div>
      <div class="mt-6 border-t border-gray-100">
        <dl class="divide-y divide-gray-100">
          <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Food Type</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ 'Hotpot' }}</dd>
          </div>
          <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Near to</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ 'Taipei Main Station' }}</dd>
          </div>
          <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Distance to <br> MRT Station</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ '30 meters' }}</dd>
          </div>
          <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Comments </dt>
            <!-- <dd class="mt-1 leading-6 sm:col-span-2 sm:mt-0"> -->
              <!-- <div>Add a comment</div> -->
            <!-- </dd> -->
          </div>
          <!-- ========== carousel component - Comment ========== -->
          <div class="max-w-full">
            <div class="carousel carousel-center p-2 space-x-4 bg-primary rounded-box">
              <div class="carousel-item">
                <div class="card w-96 bg-base-100 shadow-xl">
                  <div class="card-body">
                    <h2 class="card-title">{{ 'David Wilson' }}</h2>
                    <p>{{ 'The hotpot at this place is amazing! Highly recommended.'  }}</p>
                  </div>
                </div>
              </div>
              <div class="carousel-item">
                <div class="card w-96 bg-base-100 shadow-xl">
                  <div class="card-body">
                    <h2 class="card-title">{{ 'John Doe' }}</h2>
                    <p>{{ 'The hotpot ingredients are fresh, and the broth is rich in flavor.'  }}</p>
                  </div>
                </div>
              </div>
              <div class="carousel-item">
                <div class="card w-96 bg-base-100 shadow-xl">
                  <div class="card-body">
                    <h2 class="card-title"> &#10133; Add a comment </h2>
                    <p> Write down <br> your comments right now! </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </dl>
      </div>
    </div>
    <!-- ========== info component end ========== -->
  </div>
</template>
<script>
</script>

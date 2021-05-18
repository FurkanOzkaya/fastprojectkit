<template>
  <v-data-table
    class="table data_table"
    :headers="headers"
    :items="users">
    <template slot="item.Avatar">
     <td class="text-xs-left">
        <v-avatar size="42">
          <img src="@/assets/avatar_user.png" alt="avatar">
        </v-avatar>
      </td>
      <!-- <td class="text-xs-left">{{ props.item.address.city }}</td> -->
    </template>
  </v-data-table>
</template>

<script>

export default {
  props: ['users'],
  data() {
    return {
      headers: [
        {
          value: 'Avatar',
          align: 'left',
          sortable: false
        },
        {
          text: 'Email',
          value: 'email',
          align: 'left',
          sortable: true
        },
        {
          text: 'User Name',
          value: 'username',
          align: 'left',
          sortable: true
        },
        {
          text: 'Create Date',
          value: 'create_date',
          align: 'left',
          sortable: true
        },
        {
          text: 'Access Level',
          value: 'access_level',
          align: 'left',
          sortable: true
        }
      ]
    }
  },

  methods: {

  },

  created() {
  }
}
</script>

<style>
  .table {
    border-radius: 3px;
    background-clip: border-box;
    border: 1px solid rgba(0, 0, 0, 0.125);
    box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.21);
    background-color: transparent;
  }
  .data_table{
    width: 100%;
  }
</style>

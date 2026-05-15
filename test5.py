if (text === 'test-reminder') {
        const github = new GitHubTenantClient(github_token);
        const items = await github.getRawPendingPRsForReminder(
          github_handle,
          email,
        );

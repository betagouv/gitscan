## Changelog : cartographie (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations de stabilité et de diagnostic pour le cache des lieux, ainsi que des corrections concernant l'affichage des notifications et la gestion des erreurs du formulaire de contact. Des optimisations techniques ont également été réalisées pour l'observabilité et la journalisation.

### Évolutions fonctionnelles
- Correction d'un problème d'affichage des toasts (notifications) qui pouvaient être masqués par le modal de contact. [#94c0c6b](https://github.com/anct-cartographie-nationale/cartographie/commit/94c0c6b13b0c9618de7ce7822b3d16c9219737b0)
- Amélioration de la gestion des erreurs du formulaire de contact : les codes d'erreur du serveur sont maintenant traduits pour une meilleure compréhension par l'utilisateur. [#94c0c6b](https://github.com/anct-cartographie-nationale/cartographie/commit/94c0c6b13b0c9618de7ce7822b3d16c9219737b0)

### Évolutions techniques
- Amélioration du cache des lieux :
    - Instrumentation du cache pour faciliter le diagnostic des données obsolètes. [#052847a](https://github.com/anct-cartographie-nationale/cartographie/commit/052847a3c47a96a4b40bc93fef7a57426026576d)
    - Partage de l'instance du cache entre les différentes parties de l'application pour une meilleure cohérence. [#5053aac](https://github.com/anct-cartographie-nationale/cartographie/commit/5053aacfe4acb5f8a33a877b0770e09f1eb10f0f)
- Mise à jour des dépendances React Email pour une gestion unifiée des imports. [#7154acb](https://github.com/anct-cartographie-nationale/cartographie/commit/7154acb98641994a0528a58f788916241f48416a)
- Mise à jour des actions GitHub utilisées pour le CI/CD (actions/checkout et actions/cache). [#87ee084](https://github.com/anct-cartographie-nationale/cartographie/commit/87ee084771395763268135f6326141018131710e)
- Refactorisation de l'accès aux variables d'environnement pour utiliser la notation par points. [#f7deebe](https://github.com/anct-cartographie-nationale/cartographie/commit/f7deebe5c33757787576b225912005419496a696)

### Autres changements
- Mise à jour de la configuration de Biome pour s'aligner sur la version 2.5. [#1f3b970](https://github.com/anct-cartographie-nationale/cartographie/commit/1f3b9702b33a0f83995319f6946a22570f9d343f)
- Mise à jour de la version de la librairie `react-email`. [#7154acb](https://github.com/anct-cartographie-nationale/cartographie/commit/7154acb98641994a0528a58f788916241f48416a)

## Changelog : agora-front (30 derniers jours, au 27 août 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la clarté des textes pour les utilisateurs et la simplification de l'infrastructure technique, notamment concernant la gestion des certificats de sécurité du site.

### Évolutions fonctionnelles
- Correction des textes (wording) sur la page de modification du profil pour une meilleure compréhension [#258](https://github.com/agora-gouv/agora-front/pull/258).

### Évolutions techniques
- Simplification de la gestion des certificats SSL : migration de la configuration du challenge ACME de Nginx vers une route dédiée au sein de l'application Nuxt [#259](https://github.com/agora-gouv/agora-front/pull/259), [#261](https://github.com/agora-gouv/agora-front/pull/261), [#262](https://github.com/agora-gouv/agora-front/pull/262).
- Amélioration de la gestion des erreurs 404 lors des processus de validation de certificats [#260](https://github.com/agora-gouv/agora-front/pull/260).

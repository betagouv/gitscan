## Changelog : monlogementetudiant (30 derniers jours, au 2026-07-20)

### Résumé
Ce mois-ci, les améliorations se concentrent sur les alertes logement pour les étudiants, avec l'ajout de la gestion des préférences de notification, l'envoi d'alertes par email via Brevo, et la gestion des favoris. Des améliorations ont également été apportées à l'importation de données (RAMSES, propriétaires) et à l'interface utilisateur pour la gestion des logements et des statistiques.

### Évolutions fonctionnelles
- Les étudiants peuvent désormais gérer leurs préférences de notification. [#bc445c0](https://github.com/betagouv/monlogementetudiant/commit/bc445c0)
- Affichage d'une alerte CROUS lors de la recherche de logements. [#cf0d543](https://github.com/betagouv/monlogementetudiant/commit/cf0d543)
- Les alertes sont maintenant envoyées par email via Brevo, avec une gestion du taux d'envoi et une limitation en production. [#1b1b22d](https://github.com/betagouv/monlogementetudiant/commit/1b1b22d), [#5574a0a](https://github.com/betagouv/monlogementetudiant/commit/5574a0a), [#45a4403](https://github.com/betagouv/monlogementetudiant/commit/45a4403)
- Possibilité d'inclure les logements favoris lors de la détection de nouvelles offres. [#25c2812](https://github.com/betagouv/monlogementetudiant/commit/25c2812)
- Ajout de la gestion des types de bourses pour les utilisateurs. [#66a3042](https://github.com/betagouv/monlogementetudiant/commit/66a3042)
- Amélioration de l'affichage des alertes pour les étudiants en mode "shallow". [#bfb7989](https://github.com/betagouv/monlogementetudiant/commit/bfb7989)
- Ajout de la possibilité d'exporter des données au format CSV (départements et régions). [#aa244e4](https://github.com/betagouv/monlogementetudiant/commit/aa244e4)

### Évolutions techniques
- Migration des schémas de la base de données. [#20d699f](https://github.com/betagouv/monlogementetudiant/commit/20d699f), [#2599f2e](https://github.com/betagouv/monlogementetudiant/commit/2599f2e)
- Refonte de l'API externe et ajout d'un module de consommateurs. [#b5405d3](https://github.com/betagouv/monlogementetudiant/commit/b5405d3)
- Intégration de RAMSES (national). [#4bbb9b6](https://github.com/betagouv/monlogementetudiant/commit/4bbb9b6), [#c800cc0](https://github.com/betagouv/monlogementetudiant/commit/c800cc0)
- Amélioration de la gestion du cache pour les assets statiques de WordPress. [#61ca9bc](https://github.com/betagouv/monlogementetudiant/commit/61ca9bc), [#e9c32c1](https://github.com/betagouv/monlogementetudiant/commit/e9c32c1)
- Mise en place de jobs cron pour la détection et l'envoi des alertes. [#8e02fc1](https://github.com/betagouv/monlogementetudiant/commit/8e02fc1), [#4ebcf0b](https://github.com/betagouv/monlogementetudiant/commit/4ebcf0b)
- Correction de problèmes liés à la limite de paramètres de PostgreSQL lors de l'insertion massive d'alertes. [#83a25ed](https://github.com/betagouv/monlogementetudiant/commit/83a25ed)
- Amélioration de la sécurité en utilisant une version récente et sécurisée de `isomorphic-dompurify`. [#9f91b3e](https://github.com/betagouv/monlogementetudiant/commit/9f91b3e)

### Autres changements
- Ajout de scripts pour importer les propriétaires dans Brevo. [#0629981](https://github.com/betagouv/monlogementetudiant/commit/0629981), [#859e928](https://github.com/betagouv/monlogementetudiant/commit/859e928)
- Migration de la FAQ de Crisp vers WordPress. [#f097cee](https://github.com/betagouv/monlogementetudiant/commit/f097cee)
- Corrections de tests unitaires et d'intégration. [#fcbf628](https://github.com/betagouv/monlogementetudiant/commit/fcbf628), [#611daf5](https://github.com/betagouv/monlogementetudiant/commit/611daf5)
- Diverses corrections de bugs et améliorations de l'interface utilisateur.

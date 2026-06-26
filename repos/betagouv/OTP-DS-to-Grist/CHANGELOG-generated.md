## Changelog : OTP-DS-to-Grist (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des configurations, notamment la possibilité de gérer plusieurs configurations simultanément, de les charger et de les sauvegarder. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur. Enfin, des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer plusieurs configurations à la fois. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- Amélioration de la gestion des erreurs : les messages d'erreur persistants sont maintenant correctement affichés. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)
- Ajout de la possibilité de charger une configuration existante. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- Ajout de la possibilité de sauvegarder une seule configuration. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)
- Implémentation d'un volet dédié à la gestion des données de Démarches Simplifiées (DN). [#362](https://github.com/betagouv/OTP-DS-to-Grist/issues/362)
- Ajout d'un volet pour interagir avec Grist. [#358](https://github.com/betagouv/OTP-DS-to-Grist/issues/358)
- Correction d'un problème lié à la création d'une table répétable générique inutile. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- Amélioration du tutoriel. [#346](https://github.com/betagouv/OTP-DS-to-Grist/issues/346)
- Correction du chemin du manifest Vue.
- Mise à jour de l'interface Vue. [#340](https://github.com/betagouv/OTP-DS-to-Grist/issues/340)
- Installation de Vue.js pour le frontend. [#328](https://github.com/betagouv/OTP-DS-to-Grist/issues/328)

### Évolutions techniques
- Modification du paramètre `max_length` dans la fonction `normalize_column_name` pour une meilleure gestion des noms de colonnes. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)
- L'API gère maintenant plusieurs configurations. [#309](https://github.com/betagouv/OTP-DS-to-Grist/issues/309)
- Installation de Vue DSFR pour le frontend. [#342](https://github.com/betagouv/OTP-DS-to-Grist/issues/342)

### Autres changements
- Aucune information supplémentaire à signaler.

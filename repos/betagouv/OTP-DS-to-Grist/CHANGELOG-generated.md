## Changelog : OTP-DS-to-Grist (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des configurations de synchronisation, notamment l'ajout de fonctionnalités pour gérer plusieurs configurations simultanément, la suppression de configurations, et l'amélioration de l'interface utilisateur pour ces opérations. Des corrections de bugs et des améliorations de la robustesse ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de gérer plusieurs configurations de synchronisation (DN et Grist) via une nouvelle section dédiée. [#394](https://github.com/betagouv/OTP-DS-to-Grist/issues/394)
- Amélioration de l'affichage du statut de synchronisation, même en l'absence de configuration. [#4e49dc5](https://github.com/betagouv/OTP-DS-to-Grist/commit/4e49dc5eb03bc612af2f91cbbb1c991451a7e5fc)
- Possibilité de supprimer une configuration de synchronisation. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- Possibilité de charger une configuration de synchronisation. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- Possibilité de sauvegarder une configuration de synchronisation. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)
- Détection des dossiers supprimés via l'API DN. [#397](https://github.com/betagouv/OTP-DS-to-Grist/issues/397)
- Masquage automatique des colonnes `_id` dans Grist pour une meilleure lisibilité. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)

### Évolutions techniques
- Regroupement des logs `hide_id` sur une seule ligne pour une meilleure lisibilité des logs. [#395](https://github.com/betagouv/OTP-DS-to-Grist/issues/395)
- Suppression de la création de la table répétable générique `_repetable_rows` dans Grist. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- Suppression de la logique de troncature des valeurs de texte pour éviter les erreurs de synchronisation. [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383), [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381)
- Correction du paramètre `max_length` dans la fonction `normalize_column_name`. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)

### Autres changements
- Correction d'un bug empêchant le formulaire de configuration de se débloquer si un DN était renseigné. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Correction d'un bug lié au test de connexion DN sur une configuration déjà sauvegardée. [#391](https://github.com/betagouv/OTP-DS-to-Grist/issues/391)
- Correction d'un message d'erreur persistant. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)
- Amélioration de la gestion des erreurs lors de la synchronisation.
- Publication de la version 0.8.0. [#274](https://github.com/betagouv/OTP-DS-to-Grist/issues/274)

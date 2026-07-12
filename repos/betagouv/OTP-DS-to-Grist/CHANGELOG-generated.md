## Changelog : OTP-DS-to-Grist (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des configurations de synchronisation, avec la possibilité de gérer plusieurs configurations et de les supprimer. Des corrections de bugs améliorent la stabilité et l'expérience utilisateur, notamment en affichant correctement le statut de synchronisation et en corrigeant des blocages dans le formulaire de configuration. Des optimisations ont été apportées pour masquer automatiquement les colonnes d'identification dans Grist.

### Évolutions fonctionnelles
- Possibilité de gérer plusieurs configurations de synchronisation avec l'API OTP. [#309](https://github.com/betagouv/OTP-DS-to-Grist/issues/309)
- Ajout de la fonctionnalité de suppression d'une configuration. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- Ajout de la fonctionnalité de chargement d'une configuration. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- Ajout de la fonctionnalité de sauvegarde d'une configuration. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)
- Possibilité de synchroniser une configuration plusieurs fois. [#375](https://github.com/betagouv/OTP-DS-to-Grist/issues/375)
- Le statut de synchronisation est maintenant affiché même si la configuration associée n'existe plus. [#324](https://github.com/betagouv/OTP-DS-to-Grist/issues/324)
- Masquage automatique des colonnes contenant "_id" dans Grist. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)

### Évolutions techniques
- Correction d'un bug empêchant le formulaire de configuration de se débloquer si un DN était renseigné. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Suppression de la création de la table répétable générique `_repetable_rows` dans Grist. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- Correction d'un test de connexion DN sur une configuration déjà sauvegardée. [#391](https://github.com/betagouv/OTP-DS-to-Grist/issues/391)
- Regroupement des logs `hide_id` sur une seule ligne. [#395](https://github.com/betagouv/OTP-DS-to-Grist/issues/395)
- Suppression de la logique de troncature des valeurs de texte. [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381) et [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383)
- Correction d'un message d'erreur persistant. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)

### Autres changements
- Installation de Vue DSFR. [#342](https://github.com/betagouv/OTP-DS-to-Grist/issues/342)
- Modification du tutoriel. [#346](https://github.com/betagouv/OTP-DS-to-Grist/issues/346)
- Correction du paramètre `max_length` dans `normalize_column_name`. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)

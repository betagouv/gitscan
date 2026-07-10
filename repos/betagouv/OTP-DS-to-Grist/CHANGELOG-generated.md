## Changelog : OTP-DS-to-Grist (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des configurations de synchronisation, notamment la possibilité de gérer plusieurs configurations, de les supprimer et de les charger. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, comme la gestion du statut de synchronisation et la résolution de blocages dans le formulaire de configuration. Enfin, des optimisations ont été faites pour l'affichage des données dans Grist.

### Évolutions fonctionnelles
- Possibilité de synchroniser plusieurs configurations simultanément. [#375](https://github.com/betagouv/OTP-DS-to-Grist/issues/375)
- Ajout de la fonctionnalité de suppression d'une configuration. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- Ajout de la fonctionnalité de chargement d'une configuration. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- Possibilité de sauvegarder une configuration individuelle. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)
- Affichage du statut de synchronisation même en l'absence de configuration. [#324](https://github.com/betagouv/OTP-DS-to-Grist/issues/324)
- Correction d'un blocage du formulaire de configuration lors de la saisie du numéro DN. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Correction du test de connexion DN sur une configuration déjà sauvegardée. [#391](https://github.com/betagouv/OTP-DS-to-Grist/issues/391)
- Masquage automatique des colonnes `_id` dans Grist pour une meilleure lisibilité. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)

### Évolutions techniques
- L'API gère désormais plusieurs configurations. [#309](https://github.com/betagouv/OTP-DS-to-Grist/issues/309)
- Suppression de la création de la table répétable générique `_repetable_rows` dans Grist. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- Suppression de la logique de troncature des valeurs de texte pour éviter les erreurs. [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381) et [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383)
- Correction d'un paramètre `max_length` incorrect dans la fonction `normalize_column_name`. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)

### Autres changements
- Installation de Vue DSFR pour améliorer l'interface utilisateur. [#342](https://github.com/betagouv/OTP-DS-to-Grist/issues/342)
- Mise à jour de la documentation et du tutoriel. [#346](https://github.com/betagouv/OTP-DS-to-Grist/issues/346)
- Correction d'un message d'erreur persistant. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)
- Correction du chemin du manifest.
- Mise à jour de la vue. [#340](https://github.com/betagouv/OTP-DS-to-Grist/issues/340)

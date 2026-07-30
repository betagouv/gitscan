## Changelog : OTP-DS-to-Grist (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation des données, notamment la gestion des configurations multiples et l'affichage du statut de synchronisation. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant la gestion des erreurs et l'interface utilisateur. Enfin, des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de synchroniser plusieurs configurations. [#434](https://github.com/betagouv/OTP-DS-to-Grist/issues/434)
- Affichage du statut de synchronisation même en l'absence de configuration.
- Ajout d'une nouvelle section "DN" pour les démarches multiples. [#394](https://github.com/betagouv/OTP-DS-to-Grist/issues/394)
- Affichage de la bannière de statut de synchronisation pour les démarches multiples. [#403](https://github.com/betagouv/OTP-DS-to-Grist/issues/403)
- Ajout de la date de dernière correction en attente. [#411](https://github.com/betagouv/OTP-DS-to-Grist/issues/411)
- Amélioration des liens d'aide dans la section de synchronisation. [#423](https://github.com/betagouv/OTP-DS-to-Grist/issues/423)
- Détection des dossiers supprimés via l'API DN. [#397](https://github.com/betagouv/OTP-DS-to-Grist/issues/397)
- Masquage automatique des colonnes `_id` dans Grist. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)

### Évolutions techniques
- Mise à jour de plusieurs dépendances npm dans le frontend. [#440](https://github.com/betagouv/OTP-DS-to-Grist/issues/440)
- Mises à jour de dépendances Python (Flask, Werkzeug, etc.).
- Mises à jour de dépendances de développement (pytest, eslint, vitest, etc.).

### Autres changements
- Correction du blocage du formulaire de configuration en cas de renseignement du DN. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Correction d'un bug empêchant l'affichage du statut de synchronisation après suppression de la configuration.
- Correction d'un test de connexion DN sur une configuration déjà sauvegardée. [#391](https://github.com/betagouv/OTP-DS-to-Grist/issues/391)
- Suppression de la troncature des valeurs de texte lors de la synchronisation. [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381) et [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383)
- Correction d'un bug lié à l'URL d'aide OTP. [#410](https://github.com/betagouv/OTP-DS-to-Grist/issues/410)

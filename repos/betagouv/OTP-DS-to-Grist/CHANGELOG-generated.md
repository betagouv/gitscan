## Changelog : OTP-DS-to-Grist (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la robustesse de la synchronisation des données entre Démarches Simplifiées et Grist. Des améliorations ont été apportées à l'affichage des statuts de synchronisation, à la gestion des configurations et à la détection des suppressions de dossiers. Une nouvelle section "DN" a été ajoutée pour les démarches multiples.

### Évolutions fonctionnelles
- Ajout d'une bannière affichant le statut de la synchronisation pour les démarches multiples. [#403](https://github.com/betagouv/OTP-DS-to-Grist/issues/403)
- Ajout d'une nouvelle section "DN" pour les démarches multiples. [#394](https://github.com/betagouv/OTP-DS-to-Grist/issues/394)
- Affichage de la date de dernière correction en attente. [#411](https://github.com/betagouv/OTP-DS-to-Grist/issues/411)
- Amélioration des liens d'aide. [#423](https://github.com/betagouv/OTP-DS-to-Grist/issues/423)
- Correction de l'URL d'aide OTP. [#410](https://github.com/betagouv/OTP-DS-to-Grist/issues/410)
- Affichage du statut de synchronisation même en l'absence de configuration.
- Possibilité de synchroniser une configuration. [#375](https://github.com/betagouv/OTP-DS-to-Grist/issues/375)
- Masquage automatique des colonnes `_id` dans Grist. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)
- Détection des dossiers supprimés via l'API DN. [#397](https://github.com/betagouv/OTP-DS-to-Grist/issues/397)
- Gestion des notifications multiples. [#408](https://github.com/betagouv/OTP-DS-to-Grist/issues/408)

### Évolutions techniques
- Publication de la version 0.8.0. [#274](https://github.com/betagouv/OTP-DS-to-Grist/issues/274)
- Regroupement des logs `hide_id` sur une seule ligne pour une meilleure lisibilité. [#395](https://github.com/betagouv/OTP-DS-to-Grist/issues/395)
- Correction d'un blocage du formulaire de configuration en cas de renseignement du DN et rechargement. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Suppression de la logique de troncature des valeurs de texte, permettant de gérer les chaînes de caractères longues. [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381) et [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383)
- Correction d'un test de connexion DN sur une configuration déjà sauvegardée. [#391](https://github.com/betagouv/OTP-DS-to-Grist/issues/391)

### Autres changements
- Aucun changement significatif à signaler.

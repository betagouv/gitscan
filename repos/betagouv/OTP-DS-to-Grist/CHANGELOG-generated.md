## Changelog : OTP-DS-to-Grist (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la synchronisation des données entre Démarches Simplifiées et Grist, notamment la gestion de configurations multiples, la détection des dossiers supprimés et l'affichage d'informations de statut plus claires. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de synchroniser plusieurs configurations de données. [#375](https://github.com/betagouv/OTP-DS-to-Grist/issues/375)
- Ajout d'une nouvelle section "DN" pour la gestion des démarches. [#394](https://github.com/betagouv/OTP-DS-to-Grist/issues/394)
- Affichage d'une bannière indiquant le statut de la synchronisation, même en l'absence de configuration. [#403](https://github.com/betagouv/OTP-DS-to-Grist/issues/403) et [#324](https://github.com/betagouv/OTP-DS-to-Grist/issues/324)
- Détection des dossiers supprimés dans l'API DN pour une synchronisation plus précise. [#397](https://github.com/betagouv/OTP-DS-to-Grist/issues/397)
- Ajout de la date de dernière correction en attente. [#411](https://github.com/betagouv/OTP-DS-to-Grist/issues/411)
- Mise à jour des liens d'aide. [#423](https://github.com/betagouv/OTP-DS-to-Grist/issues/423)
- Possibilité de supprimer une configuration. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- Possibilité de charger une configuration existante. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- Possibilité de sauvegarder une configuration unique. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)

### Évolutions techniques
- Masquage automatique des colonnes `_id` dans Grist pour une meilleure organisation des données. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)
- Regroupement des logs `hide_id` sur une seule ligne pour une meilleure lisibilité. [#395](https://github.com/betagouv/OTP-DS-to-Grist/issues/395)
- Suppression de la logique de troncature des valeurs textuelles pour éviter la perte d'informations. [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383) et [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381)
- Publication de la version 0.8.0. [#274](https://github.com/betagouv/OTP-DS-to-Grist/issues/274)

### Autres changements
- Correction d'un bug empêchant le formulaire de configuration de se charger lorsque le DN était renseigné. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Correction d'un bug lié à l'affichage du message d'erreur persistant. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)
- Correction d'un test de connexion DN sur une configuration déjà sauvegardée. [#391](https://github.com/betagouv/OTP-DS-to-Grist/issues/391)
- Correction de l'affichage du statut de synchronisation même si la configuration n'existe plus.

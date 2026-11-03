## Changelog : data_pass (30 derniers jours, au 02 novembre 2026)

### Résumé
Ce mois a été marqué par un renforcement majeur des capacités de l'API, permettant désormais une gestion complète du cycle de vie des demandes (soumission, validation, métadonnées) de manière automatisée. La sécurité a également été renforcée avec la mise à jour de l'environnement Ruby et l'exigence de la double authentification pour ProConnect. Enfin, l'expérience de développement a été améliorée grâce à de nouveaux outils de test et de visualisation des composants de l'interface.

### Évolutions fonctionnelles
- **Capacités de l'API** :
    - Possibilité de soumettre et de valider des demandes directement via l'API ([#1827](https://github.com/etalab/data_pass/issues/1827)).
    - Gestion des métadonnées par les fournisseurs de données (FD) sur une demande ([#1842](https://github.com/etalab/data_pass/issues/1842)).
    - Mise en place d'une interface d'administration pour gérer les droits d'accès API par fournisseur ([#1811](https://github.com/etalab/data_pass/issues/1811)).
- **Gestion des notifications** : Les fournisseurs de données peuvent désormais désactiver certaines notifications par contrat ou via l'API ([#1841](https://github.com/etalab/data_pass/issues/1841)).
- **Interface utilisateur et formulaires** :
    - Renommage du "Contact technique" en "RSSI" dans le formulaire CISIRH ([#1802](https://github.com/etalab/data_pass/issues/1802)).
    - Ajout d'un formulaire pour demander le rôle d'administrateur Resana ([#1812](https://github.com/etalab/data_pass/issues/1812)).
    - Publication du plan d'action d'accessibilité.

### Évolutions techniques
- **Sécurité et infrastructure** :
    - Mise à jour de Ruby vers la version 4.0.9 pour corriger des vulnérabilités (CVE) ([#1836](https://github.com/etalab/data_pass/issues/1836)).
    - Rendre la double authentification (2FA) ProConnect obligatoire pour tous les agents ([#1809](https://github.com/etalab/data_pass/issues/1809)).
    - Blocage de l'indexation par les moteurs de recherche des pages publiques des demandes ([#1829](https://github.com/etalab/data_pass/issues/1829)).
- **API et Webhooks** :
    - Amélioration de la fiabilité des webhooks lors des écritures par API, incluant désormais la source et les métadonnées ([#1843](https://github.com/etalab/data_pass/issues/1843)).
    - Meilleure traçabilité des actions effectuées via l'API dans l'historique des demandes.
- **Expérience développeur (DX)** :
    - Intégration de "Lookbook" pour permettre une prévisualisation isolée des composants de l'interface ([#1832](https://github.com/etalab/data_pass/issues/1832), [#1833](https://github.com/etalab/data_pass/issues/1833), [#1814](https://github.com/etalab/data_pass/issues/1814)).
    - Création d'un script pour faciliter la construction des branches de recette sandbox ([#1816](https://github.com/etalab/data_pass/issues/1816)).

### Autres changements
- **Documentation** :
    - Mise à jour de la documentation OpenAPI et des spécifications techniques de l'API.
    - Formalisation des règles de contribution de l'équipe technique ([#1787](https://github.com/etalab/data_pass/issues/1787)).
- **Maintenance** : Optimisation et refactorisation des jeux de données de test (seeds).

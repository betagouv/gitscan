## Changelog : django-lasuite (30 derniers jours, au 15/10/2026)

### Résumé
Cette période a été marquée par l'introduction d'un nouveau moteur de détection de malwares (ICAP) et par des améliorations de sécurité significatives. Les évolutions concernent tant la fiabilité de l'authentification (OIDC) que la protection des données personnelles et la robustesse de l'analyse de fichiers.

### Évolutions fonctionnelles
- **Détection de malwares** : Ajout d'un backend ICAP pour permettre le scan de fichiers via un moteur antivirus compatible et amélioration de la détection des infections via les en-têtes ICAP.
- **Authentification (OIDC)** : 
    - Support de la méthode POST pour les demandes de déconnexion initiées par le client (RP-initiated logout).
    - Amélioration de la gestion des états de rappel (callback) pour traiter plus sereinement les rejeux de requêtes.
- **Marketing** : Correction d'une fuite de données personnelles (PII) dans les logs du backend Brevo.

### Évolutions techniques
- **Refonte du module Malware** : 
    - Restructuration de l'architecture avec l'introduction d'une classe de base (`BaseBackend`) pour uniformiser la gestion des enregistrements.
    - Migration vers des méthodes abstraites pour la gestion des tâches d'analyse.
    - Optimisation de la manipulation des chemins de fichiers via l'utilisation de `PurePath`.
- **Sécurité** : Renforcement de la sécurité des communications en imposant un protocole TLS 1.2 minimum pour les contextes SSL ICAP.
- **Qualité et Tests** : 
    - Augmentation de la couverture de tests pour le backend ICAP (gestion des doublons et des mécanismes de tentatives de reconnexion).
    - Enregistrement des tâches de scan ICAP dans le package des tâches asynchrones.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique du backend suite aux refontes structurelles.
- **Maintenance** : Nettoyage du dépôt (suppression de templates locaux, de commentaires inutiles et mise à jour du `.gitignore`).

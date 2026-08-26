## Changelog : messages (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur le renforcement de la sécurité de la messagerie (protocoles SPF, DKIM et JMAP) et l'amélioration de la fiabilité des échanges. L'expérience utilisateur a également été affinée, notamment via des corrections d'interface et une meilleure gestion de la déconnexion sur les applications mobiles.

### Évolutions fonctionnelles
- **Expérience Mobile** : Amélioration du processus de déconnexion pour assurer la fermeture complète de la session auprès du fournisseur d'identité.
- **Interface Utilisateur** : 
    - Optimisation de l'affichage des extraits de messages et des fils de discussion.
    - Masquage des statistiques dans le dossier "Envoyés" pour épurer l'interface.
    - Correction de l'affichage de l'autosave qui apparaissait lors de l'envoi d'un message.
    - Limitation de l'éditeur de texte aux couleurs autorisées.
- **Corrections de bugs** :
    - Résolution d'un problème de suivi des fils de discussion lorsque le sujet d'un email est modifié [#765].
    - Correction d'un conflit technique (race condition) lors de l'envoi de messages impliquant plusieurs destinataires.

### Évolutions techniques
- **Sécurité de la messagerie** :
    - Renforcement de la sécurité du protocole JMAP (parsing et composition) avec le passage à la version 0.3.0.
    - Amélioration de la fiabilité de la vérification SPF [#782] et assouplissement des règles de vérification DKIM [#778].
    - Durcissement de la sécurité de `pymta` via l'ajout de nouveaux paramètres et limites [#777].
- **Infrastructure et Provisioning** :
    - Mise à jour de Keycloak vers les versions 26.7.1 et 26.7.2 [#776, #784].
    - Ajout d'un point de terminaison permettant de lister les enregistrements DNS pour l'ensemble des domaines [#780].
- **Architecture Mobile** : Migration de la configuration de l'identité et du schéma d'authentification vers un pilotage par variables d'environnement.

### Autres changements
- **Documentation** : Ajout d'un guide de configuration pour le fournisseur d'identité (Keycloak) [#781].
- **Interface** : Mise à jour du titre de la documentation.

## Changelog : messages (30 derniers jours, au 29 août 2026)

### Résumé
Les évolutions de ce mois se sont concentrées sur le renforcement de la fiabilité et de la sécurité de la gestion des emails (protocoles SPF, DKIM et parsing), l'amélioration de l'expérience utilisateur sur mobile et l'optimisation de l'interface pour une navigation plus fluide et cohérente.

### Évolutions fonctionnelles
- **Messagerie** : Support des adresses email internationalisées et passage systématique des boîtes aux lettres en minuscules [#785].
- **Expérience Mobile** : Amélioration du processus de déconnexion pour garantir la fermeture complète de la session auprès du fournisseur d'identité.
- **Interface Utilisateur** :
    - Optimisation de l'affichage des extraits de messages et des fils de discussion.
    - Masquage des statistiques du dossier "Envoyés" pour épurer l'interface.
    - Restriction des couleurs dans l'éditeur de texte pour garantir la cohérence visuelle.
    - Correction du comportement de l'enregistrement automatique lors de l'envoi d'un message.
- **Administration** : Ajout d'une fonctionnalité permettant de lister les enregistrements DNS pour l'ensemble des domaines [#780].
- **Corrections** : 
    - Résolution d'un problème de suivi des fils de discussion lorsque le sujet d'un email est modifié [#765].
    - Correction de conflits (race conditions) lors de l'envoi de messages avec plusieurs destinataires.

### Évolutions techniques
- **Sécurité et Protocoles Email** :
    - Renforcement du composant `pymta` via l'ajout de nouvelles limites, de configurations et d'une meilleure journalisation [#777, #783].
    - Amélioration de la robustesse du vérificateur SPF pour couvrir davantage de cas particuliers [#782].
    - Assouplissement de la vérification des espaces blancs pour les configurations DKIM [#778].
    - Sécurisation du parsing et de la composition des messages pour mieux résister aux emails malveillants.
- **Infrastructure Mobile** : Migration de la gestion de l'identité et du schéma d'authentification vers un modèle piloté par les variables d'environnement.

### Autres changements
- **Documentation** : Ajout d'un guide de configuration pour le fournisseur d'identité (Identity Provider) [#781] et mise à jour des titres de la documentation.

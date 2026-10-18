## Changelog : hubee (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, Hubee a considérablement enrichi ses capacités d'échange documentaire. Les utilisateurs peuvent désormais télécharger plus facilement les pièces reçues, accéder à des archives de documents et interagir avec les dossiers en envoyant des pièces jointes lors des changements d'état. L'interface a également été simplifiée et clarifiée pour offrir une navigation plus intuitive.

### Évolutions fonctionnelles
- **Gestion documentaire améliorée** : 
    - Possibilité de télécharger les pièces jointes reçues et d'accéder à une archive regroupant les documents d'un télédossier.
    - Capacité d'envoyer des pièces jointes et des messages lors des changements d'état d'un dossier.
    - Ajout de liens de téléchargement conformes aux standards DSFR.
- **Expérience utilisateur et interface** :
    - Adoption de la terminologie "télédossiers" pour plus de clarté.
    - Amélioration de la visibilité des informations (noms des flux, états des dossiers, et messages d'erreur explicites).
    - Ajout d'un bandeau d'information pour orienter les utilisateurs vers le support de la version bêta.
    - Meilleure gestion de la liste des abonnements de la structure.
- **Nouveaux workflows** :
    - Possibilité d'accuser réception d'un nouveau télédossier.
    - Possibilité de faire progresser un dossier directement depuis sa vue détaillée.

### Évolutions techniques
- **Observabilité et traçabilité** :
    - Refonte du système de journalisation (logs) pour inclure l'adresse IP, les exceptions et les redirections sur une seule ligne, facilitant le diagnostic.
    - Amélioration du suivi des erreurs via Sentry pour les environnements de revue (review apps).
- **Performance et robustesse** :
    - Optimisation des connexions à la base de données PostgreSQL (limitation des temps de connexion et connexion prioritaire au nœud primaire).
    - Amélioration de la gestion des erreurs pour afficher des pages HTML sans solliciter la base de données.
    - Mise en cache des abonnements pour améliorer la réactivité du portail.
- **Infrastructure et sécurité** :
    - Sécurisation des conteneurs par l'utilisation d'images Docker "distroless".
    - Refactorisation de la gestion des flux et des habilitations pour une architecture plus propre.

### Autres changements
- **Documentation** : Mise à jour des explications concernant l'authentification et le fonctionnement interne de la recherche de pièces jointes.
- **Qualité et tests** : Renforcement des tests automatisés de bout en bout, notamment sur les processus de téléchargement et de gestion des archives.

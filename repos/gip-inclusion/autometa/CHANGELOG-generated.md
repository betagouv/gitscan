## Changelog : autometa (30 derniers jours, au 13 novembre 2026)

### Résumé
L'assistant IA gagne en intelligence, en fiabilité et en ergonomie. Les utilisateurs bénéficient de nouvelles capacités d'interaction (GitHub, PDF, Slack, Notion), d'une interface mobile optimisée et d'un meilleur suivi des tableaux de bord. En parallèle, le système a été considérablement renforcé sur le plan de la sécurité et de la stabilité technique, notamment pour la gestion des connexions et des tâches automatisées.

### Évolutions fonctionnelles
- **Intelligence Artificielle & Skills** : 
    - Ajout de nouvelles capacités : interaction avec GitHub [#281], lecture de fichiers PDF [#284] et gestion améliorée des bases de données [#283].
    - Amélioration de la pertinence des réponses grâce à un enrichissement des instructions de l'agent sur le contexte métier et les outils de production.
    - Possibilité pour l'agent d'écrire directement dans Slack et Notion [#277].
- **Gestion des Tableaux de Bord** : 
    - Mise en place d'alertes pour signaler les tableaux de bord obsolètes ou nécessitant une republication [#260].
    - Vérification de la qualité visuelle avant le partage de liens [#230] et description détaillée des calculs métier [#288].
- **Expérience Utilisateur (UX)** : 
    - Optimisation de l'interface mobile (en-têtes, champs de saisie et navigation) [#303].
    - Amélioration de la recherche de conversations par mots-clés [#274] et épinglage du guide de données dans la navigation [#234].
    - Gestion des macros Zendesk pour permettre la lecture et l'édition de changements réversibles [#bfd93a3].

### Évolutions techniques
- **Sécurité** : 
    - Renforcement de la protection des données : masquage des secrets dans les logs [#294], transfert sécurisé des jetons Matomo via le corps des requêtes [#296] et restriction des accès aux conversations [#83fb971].
    - Sécurisation de l'environnement : interdiction d'installations logicielles non autorisées dans les conteneurs [#297] et correction de vulnérabilités (Log Injection).
- **Stabilité & Performance** : 
    - Amélioration de la résilience de Redis (gestion des timeouts et des erreurs de connexion) pour éviter les blocages du système.
    - Fiabilisation des tâches de fond (cron) et gestion des messages en attente côté serveur [#298, #272].
    - Optimisation des performances via la parallélisation des tests et l'optimisation de l'image Scalingo [#266].
- **Architecture** : 
    - Mise en place de dossiers de travail privés par conversation pour une meilleure isolation des données [#295].
    - Amélioration du processus de déploiement et de gestion des environnements de test (review-apps).

### Autres changements
- Amélioration des processus de validation interne (Definition of Done) et de l'audit des conversations.
- Nettoyage et formatage du code (Ruff).

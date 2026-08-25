## Changelog : iterion (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois a été marqué par un effort massif sur la fiabilité et la visibilité du système. L'introduction de "Goldy" (un système de test de non-régression comportementale) et du bot "Endy" (couverture de tests de bout en bout) renforce la stabilité des agents. Parallèlement, de nouvelles capacités de contrôle ont été ajoutées, notamment une gestion fine des quotas de consommation (usage-caps) et une meilleure visibilité sur les coûts et les modèles utilisés, permettant un pilotage plus précis des workflows d'IA.

### Évolutions fonctionnelles
- **Nouveautés majeures** :
    - Introduction de **Goldy (Golden Master)** : un système de test de non-régression comportementale qui permet de valider que les agents se comportent toujours comme prévu, incluant désormais la capture de documents (PDF, tableurs) [#27, #30].
    - Gestion des **Usage-caps** : possibilité de définir, consulter et administrer les limites de consommation (budgets) en temps réel via la CLI et l'API [#9].
    - Support du backend **Pi** : intégration de Pi comme moteur d'exécution de premier rang [#308].
    - Serveur **MCP (Model Context Protocol)** : déploiement d'un serveur opérateur permettant d'exposer les capacités d'Iterion localement ou à distance [#421].
    - Optimisation du **Studio** : ajout de l'aperçu des contenus (JSON, Markdown, texte) lors des étapes de validation humaine [#425] et interface de pipeline redimensionnable [#335].
    - Mutualisation des ressources : possibilité de partager les quotas LLM inutilisés entre les contributeurs d'une équipe [#350].
- **Améliorations et corrections** :
    - Meilleure transparence sur l'exécution : affichage du modèle réellement utilisé et des coûts associés dans le Studio et la console [#474, #472].
    - Amélioration de la gestion des sessions : les exécutions interrompues peuvent désormais être reprises plus efficacement [#470, #449].
    - Correction de la gestion des erreurs dans le flux de données (feed-watch) pour éviter les alertes injustifiées [#456].

### Évolutions techniques
- **Architecture et Runtime** :
    - Implémentation du mode **"Lame-duck drain"** : permet de terminer proprement les exécutions en cours lors d'un déploiement, évitant ainsi les interruptions brutales [#467].
    - Renforcement de la **sécurité des Sandboxes** : amélioration de l'isolation (gestion des certificats JVM, politiques réseau, protection accrue des tokens et des secrets) [#466, #468].
    - Gestion dynamique des identifiants : possibilité de faire pivoter les clés d'accès aux LLM de la plateforme sans nécessiter de redéploiement [#466].
    - Optimisation du stockage : meilleur nettoyage automatique des espaces de travail (worktrees) et gestion plus fine des fichiers temporaires [#469, #477].
- **Qualité et Tests** :
    - Déploiement de **Endy** : un bot dédié à la couverture de tests de bout en bout (e2e) qui analyse la matrice des fonctionnalités pour identifier les zones non couvertes [#fa20d7a].
    - Amélioration de la robustesse des tests de non-régression avec des rapports de mutation plus précis [#383].

### Autres changements
- **Documentation** : mise à jour massive de la documentation technique, incluant les guides MCP, les bilans de campagnes d'agents, et les procédures de gestion des identifiants cloud.
- **Infrastructure** : mise à jour des images de base Docker et optimisation des pipelines CI/CD.
- **Maintenance** : transition de la gestion des dépendances vers l'application interne `socialgouv-renovate` [#509].

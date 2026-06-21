## Changelog : dahlia (30 derniers jours, au 20 juin 2026)

### Résumé
Le projet Dahlia a connu une progression significative au cours des dernières semaines, avec l'ajout de nombreuses fonctionnalités clés pour la gestion des dossiers DALO, DAHO et DAHU. Les améliorations portent notamment sur la recherche, le tri, l'anonymisation des données, l'intégration du SSO ProConnect et l'automatisation de la synchronisation des dossiers. L'application est désormais plus robuste et offre une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Recherche et Tri:** Ajout de la recherche et du tri dans les tableaux des pièces et de l'historique des dossiers [#22]. Amélioration de la recherche et du tri des dossiers en général [#19].
- **Gestion des dossiers:** Ajout d'un bouton pour rafraîchir les informations d'un dossier et amélioration de l'accessibilité des dossiers supprimés [#16].
- **Détails des dossiers:** Ajout de détails supplémentaires dans les dossiers pour une meilleure compréhension [#13].
- **Scrapping et Synchronisation:** Implémentation d'un scrapping de tous les types de dossiers avec anonymisation des données [#6, #5].  Ajout d'une synchronisation automatique des dossiers chaque nuit [#12]. Amélioration de la robustesse du scrapping avec un système de ré-essai en cas d'erreurs temporaires [#8].
- **Authentification:** Intégration du SSO ProConnect pour l'authentification des utilisateurs [#7].
- **Indicateurs visuels:** Ajout d'un badge "très urgent" pour signaler les dossiers prioritaires [#21] et d'un bandeau indiquant que l'application n'est pas en production [#20].

### Évolutions techniques
- **Déploiement:** Mise en place d'un script pour la création de releases et le déploiement en production [#17].  Configuration du déploiement sur Scalingo [#3].
- **Anonymisation:** Amélioration de l'anonymisation des données, notamment en fonction de l'environnement [#14, #11].
- **Infrastructure:** Ajout de `ts-node` en production pour permettre l'exécution du scraping [#9].
- **Qualité du code:** Mise en forme du code avec Prettier et Linter pour améliorer la lisibilité et la maintenabilité [#15].
- **CI/CD:** Correction du workflow de déploiement pour assurer le bon checkout du code [#4].

### Autres changements
- Correction d'un problème de déconnexion intempestive après la connexion [#10].
- Correction d'un problème avec le paramètre 'directory' pour dependabot [#24].
- Utilisation de npm comme gestionnaire de package pour dependabot [#2].
- Création de la première version de l'application web Dahlia [#1].

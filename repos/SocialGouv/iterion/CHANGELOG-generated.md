## Changelog : iterion (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois a été marqué par une montée en maturité majeure avec le lancement de l'épic "Assistant Iterion" [#480](https://github.com/SocialGouv/iterion/issues/480). Le projet a considérablement renforcé ses capacités d'orchestration grâce à un nouveau contrat public pour le langage de description (DSL) et une meilleure gestion des agents multi-fichiers. L'expérience utilisateur a été enrichie par des outils de revue de code assistés par IA (Revi) plus détaillés et une interface Studio repensée pour l'orchestration. Enfin, la gestion des coûts et des quotas est devenue plus granulaire et transparente pour les administrateurs.

### Évolutions fonctionnelles
- **Intelligence Artificielle & Revue :**
    - Lancement de l'épic "Assistant Iterion" pour une assistance accrue dans les workflows [#480](https://github.com/SocialGouv/iterion/issues/480).
    - Amélioration de l'agent de revue de code **Revi** : affichage de détails de runs liés et intégration de vues compressées dans le footer des revues [#1173](https://github.com/SocialGouv/iterion/issues/1173), [#1167](https://github.com/SocialGouv/iterion/issues/1167).
    - Introduction de **Senti**, un agent de surveillance des vulnérabilités basé sur l'inventaire sans recours systématique aux LLM [#515](https://github.com/SocialGouv/iterion/issues/515).
- **Langage de description (DSL) & Bots :**
    - Mise en place du "contrat public" pour les bots : définition claire des déclarations, liaisons, et lecteurs (readers) [#1263](https://github.com/SocialGouv/iterion/issues/1263).
    - Support de l'importation de bots répartis sur plusieurs fichiers pour une meilleure modularité [#1225](https://github.com/SocialGouv/iterion/issues/1225).
    - Ajout d'une galerie de modèles de bots via la commande `bots create --template` dans le Studio [#1114](https://github.com/SocialGouv/iterion/issues/1114).
- **Interface & Studio :**
    - Refonte de l'accueil Cloud du Studio pour se concentrer sur l'orchestration des workflows [#1028](https://github.com/SocialGouv/iterion/issues/1028).
    - Amélioration de la visibilité des capacités des modèles (prix et sortie maximale) dans l'interface [#575](https://github.com/SocialGouv/iterion/issues/575).
- **Gestion des ressources & Quotas :**
    - Introduction de niveaux de revue par dépôt (glance / guard / audit) [#742](https://github.com/SocialGouv/iterion/issues/742).
    - Nouvelle API pour la gestion des quotas d'utilisation en temps réel par les super-administrateurs [#...](https://github.com/SocialGouv/iterion/issues/...).
    - Meilleure traçabilité de la facturation par dépôt et par niveau de service [#1105](https://github.com/SocialGouv/iterion/issues/1105).

### Évolutions techniques
- **Runtime & Exécution :**
    - Renforcement de l'isolation des bundles de sous-bots sur l'ensemble des runners [#1195](https://github.com/SocialGouv/iterion/issues/1195).
    - Optimisation de la gestion des budgets et des tentatives de reconnexion (retries) lors des échecs de runs [#...](https://github.com/SocialGouv/iterion/issues/...).
    - Amélioration de la gestion des worktrees pour permettre des lancements CLI ciblés sur des dépôts spécifiques [#1161](https://github.com/SocialGouv/iterion/issues/1161).
- **Infrastructure & CI/CD :**
    - Création d'une image de runner ARC versionnée avec support `cgo` pour les besoins de compilation [#1202](https://github.com/SocialGouv/iterion/issues/1202).
    - Optimisation de la file d'attente de fusion (merge queue) pour ne lancer que les tests critiques [#975](https://github.com/SocialGouv/iterion/issues/975).
    - Mise en place de l'exécution parallèle des suites de tests E2E pour réduire les temps de CI [#880](https://github.com/SocialGouv/iterion/issues/880).
- **Sécurité :**
    - Correction de vulnérabilités CSRF sur les endpoints de l'API [#1058](https://github.com/SocialGouv/iterion/issues/1058).
    - Amélioration de la gestion des secrets et de l'audit des credentials OAuth [#819](https://github.com/SocialGouv/iterion/issues/819).

### Autres changements
- **Documentation :** Refonte de la structure documentaire (séparation de `CLAUDE.md` en arbre de doctrine) [#1231](https://github.com/SocialGouv/iterion/issues/1231) et mise à jour des guides de déploiement Cloud [#832](https://github.com/SocialGouv/iterion/issues/832).
- **Branding :** Déploiement de la nouvelle identité visuelle avec la mascotte Iterion-bot sur l'ensemble des composants (avatars, favicons, logos) [#794](https://github.com/SocialGouv/iterion/issues/794).

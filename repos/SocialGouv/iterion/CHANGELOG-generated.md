## Changelog : iterion (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de la structure du langage de programmation d'Iterion (DSL), passant à une version beaucoup plus robuste et prévisible. L'écosystème s'est considérablement enrichi avec l'arrivée de nombreux nouveaux agents spécialisés (bots) pour l'audit, la revue de code et le développement. Parallèlement, l'interface de gestion (Studio) a été refondue pour offrir un contrôle administratif plus fin sur les équipes, la consommation des crédits et l'orchestration des tâches.

### Évolutions fonctionnelles
- **Expansion du catalogue d'agents :** Déploiement de plusieurs vagues de nouveaux bots spécialisés, notamment pour la revue de Pull Requests, le développement de fonctionnalités, l'audit de sécurité et la gestion de campagnes ([#1344](https://github.com/SocialGouv/iterion/issues/1344)).
- **Refonte de l'interface Studio :** 
    - Nouvelle page d'accueil du Cloud centrée sur l'orchestration.
    - Introduction d'une vue "Source" par fichier pour une meilleure inspection du code des agents.
    - Amélioration de la navigation et de la gestion des onglets de projet.
- **Administration et Gouvernance :**
    - Nouveaux tableaux de bord pour la gestion des équipes et des membres depuis la console Cloud ([#1559](https://github.com/SocialGouv/iterion/issues/1559)).
    - Suivi détaillé de la consommation des crédits et des limites d'utilisation de la plateforme ([#1442](https://github.com/SocialGouv/iterion/issues/1442), [#1444](https://github.com/SocialGouv/iterion/issues/1444)).
    - Possibilité pour une organisation de partager ses propres clés LLM avec ses équipes ([#1000](https://github.com/SocialGouv/iterion/issues/1000)).
- **Nouveaux agents spécialisés :** Intégration de nouveaux modèles d'assistance comme Revi, Billy, Vetty et Senti pour des missions de surveillance et d'analyse.

### Évolutions techniques
- **Migration majeure du DSL (Profil 2) :** Refonte complète du langage de description pour inclure une validation plus stricte à la compilation, une gestion améliorée des variables et un outil de migration automatique (`iterion dsl migrate`) ([#1010](https://github.com/SocialGouv/iterion/issues/1010)).
- **Optimisation du Runtime et de l'Exécution :**
    - Amélioration de l'isolation des sous-agents (subbots) via des environnements sécurisés (sandboxes).
    - Renforcement des capacités de reprise après interruption (checkpoint/resume) pour les exécutions de workflows ([#988](https://github.com/SocialGouv/iterion/issues/988)).
    - Gestion plus fine des budgets et des quotas lors de l'exécution des nœuds.
- **Infrastructure et Cloud :**
    - Amélioration du déploiement Kubernetes avec une meilleure gestion des ressources (requests/limits) et de la répartition des pods ([#694](https://github.com/SocialGouv/iterion/issues/694), [#802](https://github.com/SocialGouv/iterion/issues/802)).
    - Support des runners auto-hébergés pour les processus de CI.
- **Sécurité et Authentification :**
    - Correction de failles de sécurité (CSRF) sur l'API ([#1058](https://github.com/SocialGouv/iterion/issues/1058)).
    - Renforcement de la gestion des secrets et des permissions d'accès aux credentials ([#1863](https://github.com/SocialGouv/iterion/issues/1863)).
- **Connecteurs :** Mise en place d'un catalogue de connecteurs plus déterministe ([#1119](https://github.com/SocialGouv/iterion/issues/1119)).

### Autres changements
- **Identité visuelle :** Introduction de la mascotte officielle d'Iterion sur l'ensemble de la plateforme (avatars, icônes, logos) ([#794](https://github.com/SocialGouv/iterion/issues/794)).
- **Documentation :** Mise à jour importante de la documentation technique et ajout de guides de comparaison de produits en français ([#1129](https://github.com/SocialGouv/iterion/issues/1129)).

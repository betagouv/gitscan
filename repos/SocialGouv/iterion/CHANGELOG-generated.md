## Changelog : iterion (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, Iterion a franchi une étape clé dans la maturité de son orchestration d'agents IA. Les évolutions majeures se concentrent sur l'intelligence du routage des modèles (LLM routing), le renforcement de la sécurité via un isolation accrue des environnements d'exécution (sandboxing) et l'enrichissement des capacités d'administration pour les gestionnaires de plateformes. La gestion des ressources et des budgets a également été affinée pour offrir un contrôle plus granulaire sur les coûts et la souveraineté des données.

### Évolutions fonctionnelles
- **Routage intelligent des modèles (LLM Routing) :** Introduction d'une politique de routage adaptative permettant des configurations personnalisées (overrides) par modèle ou fournisseur, avec une gestion fine au niveau de l'organisation et de l'équipe [#2586](https://github.com/SocialGouv/iterion/issues/2586) ([#2210](https://github.com/SocialGouv/iterion/issues/2210), [#2126](https://github.com/SocialGouv/iterion/issues/2126), [#2159](https://github.com/SocialGouv/iterion/issues/2159)).
- **Administration et Studio :** 
    - Ajout de nouveaux écrans d'administration pour la gestion des rôles de bots, des variables de sandbox et des credentials de la plateforme [#1443](https://github.com/SocialGouv/iterion/issues/1443) ([#1461](https://github.com/SocialGouv/iterion/issues/1461)).
    - L'inspecteur de workflow permet désormais d'éditer directement les permissions des outils [#2383](https://github.com/SocialGouv/iterion/issues/2383).
    - Amélioration de la gestion des webhooks et des postures de fusion (merge-gate) depuis le Studio [#2479](https://github.com/SocialGouv/iterion/issues/2479).
- **Gestion des Bots et GitOps :** Mise à jour de GitOps-warden (v0.2.0) incluant des verdicts en français, le rendu Helm et des liens directs vers les runs [#2389](https://github.com/SocialGouv/iterion/issues/2389). Amélioration de la navigation dans le catalogue des bots par catégories et tags [#1520](https://github.com/SocialGouv/iterion/issues/1520).
- **Contrôle des ressources et budgets :** 
    - Possibilité de réserver une capacité de budget spécifique pour une charge de travail plutôt que de simplement la plafonner [#1099](https://github.com/SocialGouv/iterion/issues/1099).
    - Option de mise en pause automatique d'un run dès que son plafond de budget est atteint [#2263](https://github.com/SocialGouv/iterion/issues/2263).
- **Expérience Développeur (DSL & CLI) :** 
    - Amélioration du langage DSL avec une validation plus stricte des contraintes de variables au lancement et une meilleure préservation des commentaires lors de la mise en forme [#2328](https://github.com/SocialGouv/iterion/issues/2328), [#1628](https://github.com/SocialGouv/iterion/issues/1628), [#1616](https://github.com/SocialGouv/iterion/issues/1616).
    - Nouvelle commande CLI pour reprendre massivement tous les runs bloqués par l'usage, avec un filtrage par code d'erreur [#2249](https://github.com/SocialGouv/iterion/issues/2249).

### Évolutions techniques
- **Sécurité et Isolation (Sandboxing) :** 
    - Renforcement massif de l'isolation des processus : refus des liens symboliques (symlinks), isolation des credentials et de l'egress LLM, et protection contre les redirections de l'environnement hôte [#2310](https://github.com/SocialGouv/iterion/issues/2310), [#2339](https://github.com/SocialGouv/iterion/issues/2339), [#2321](https://github.com/SocialGouv/iterion/issues/2321), [#2325](https://github.com/SocialGouv/iterion/issues/2325), [#2472](https://github.com/SocialGouv/iterion/issues/2472), [#2478](https://github.com/SocialGouv/iterion/issues/2478).
    - Implémentation du "scellement souverain" pour les secrets et les pools, garantissant que les clés de chiffrement restent hors des pods [#2236](https://github.com/SocialGouv/iterion/issues/2236).
- **Infrastructure et Cloud :** 
    - Introduction de pools de runners souverains (un déploiement par pool) [#2273](https://github.com/SocialGouv/iterion/issues/2273).
    - Adoption de SeaweedFS comme stockage d'objets pour l'environnement de développement [#1943](https://github.com/SocialGouv/iterion/issues/1943), [#2089](https://github.com/SocialGouv/iterion/issues/2089).
- **Fiabilité et CI/CD :** 
    - Mise en place de sondes de santé pour surveiller les délais d'exécution des runners [#2578](https://github.com/SocialGouv/iterion/issues/2578).
    - Amélioration de la détection des régressions d'accessibilité (a11y) dans le Studio [#2347](https://github.com/SocialGouv/iterion/issues/2347).
    - Optimisation de la CI avec un partitionnement déterministe des tests et une meilleure gestion du parallélisme [#2568](https://github.com/SocialGouv/iterion/issues/2568), [#2213](https://github.com/SocialGouv/iterion/issues/2213).
- **Gestion des flux et identités :** Les commandes du plan de contrôle et les baux (leases) de run portent désormais l'identité admise du run pour une meilleure traçabilité [#2270](https://github.com/SocialGouv/iterion/issues/2270), [#2266](https://github.com/SocialGouv/iterion/issues/2266).

### Autres changements
- **Documentation :** Refonte majeure de la documentation technique incluant des diagrammes de base de données (ERD) complets et zoomables en SVG [#2582](https://github.com/SocialGouv/iterion/issues/2582), [#2579](https://github.com/SocialGouv/iterion/issues/2579), ainsi que des cartes visuelles des flux de fonctionnalités [#2561](https://github.com/SocialGouv/iterion/issues/2561).
- **Documentation :** Mise à jour des guides sur la structure des domaines et des sessions interactives des agents [#2106](https://github.com/SocialGouv/iterion/issues/2106), [#2070](https://github.com/SocialGouv/iterion/issues/2070).

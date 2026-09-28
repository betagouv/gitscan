## Changelog : iterion (30 derniers jours, au 27 septembre 2026)

### Résumé
Ce mois a été marqué par une étape majeure de modernisation de la plateforme. L'accent a été mis sur la robustesse du langage de définition des agents (DSL) et sur l'automatisation des processus de mise à niveau. L'expérience utilisateur a été enrichie par de nouveaux agents spécialisés (audit, revue de code, surveillance) et par une interface de gestion (Studio) plus complète, permettant un contrôle fin des ressources et des accès.

### Évolutions fonctionnelles
- **Nouveaux agents et capacités :**
    - Introduction de l'agent **Argus** pour la surveillance déterministe des processus [#1869].
    - Ajout de l'agent **Assessment** capable de générer automatiquement les contrats d'exécution pour les campagnes [#1776].
    - Amélioration des capacités de revue de code avec l'agent **Revi**, incluant désormais des détails sur les exécutions liées [#1173, #1167].
    - Déploiement de capacités d'audit de sécurité profond (deep scan) pour les sources et les dépendances [#1347, #1141, #1104].
- **Améliorations du Studio (Interface) :**
    - Nouvelle vue "Source" par fichier, incluant le contrôle des permissions des nœuds et la réparation via le cloud [#1738].
    - Optimisation de la gestion des onglets et de la navigation entre les projets [#1840, #1830].
    - Ajout d'écrans d'administration pour le suivi de la consommation des crédentials et des capacités de la plateforme [#1444, #1442, #1441].
- **Administration et Cloud :**
    - Gestion directe des équipes et des membres depuis la console cloud [#1559].
    - Refonte de la page d'accueil du Studio pour se concentrer sur l'orchestration [#1028].
    - Mise en place d'un système de gestion des abonnements et des paliers (tiers) pour les fournisseurs [#1818].

### Évolutions techniques
- **Refonte du DSL (Langage Déclaratif) :**
    - Déploiement massif de la "Lot 5" du DSL : amélioration de l'admission, du transport, de la validation et génération de schémas JSON [#1720, #1664, #1584, #1631].
    - Migration vers le profil de syntaxe `dsl: 2` pour une meilleure précision lexicale [#1154].
    - Amélioration de la validation à la compilation pour les variables et les contraintes de groupe [#1660, #1628].
- **Runtime et Exécution :**
    - Renforcement de l'isolation des sandboxes et de la gestion des worktrees pour garantir que l'exécution ne modifie que son propre environnement [#1889, #1806, #1303].
    - Optimisation de la gestion des processus de "fan-out" et de "convergence" dans les workflows complexes [#1193, #1187].
    - Amélioration de la résilience des exécutions lors des reprises (resume) après échec [#1490, #988].
- **Sécurité et Infrastructure :**
    - Amélioration du cloisonnement des tokens et des credentials par équipe et par organisation [#1880, #1670, #1065].
    - Renforcement de la sécurité des endpoints OAuth et de l'audit des credentials refusés [#819, #1863].
    - Optimisation des déploiements Kubernetes (gestion des `priorityClassName` et des ressources des pods) [#802, #694].

### Autres changements
- **Documentation :** Mise à jour importante des guides sur le DSL, les processus de déploiement cloud et les politiques de comparaison de produits [#1342, #832, #1142, #1129].
- **Identité visuelle :** Intégration de la nouvelle mascotte d'Iterion sur l'ensemble de la plateforme (avatars, favicons, logos) [#794].

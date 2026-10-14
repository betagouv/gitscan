## Changelog : iterion (30 derniers jours, au 13 octobre 2026)

### Résumé
Iterion a franchi une étape majeure dans la maturité de son orchestration d'agents. Les évolutions récentes se concentrent sur la simplification de la création de processus via un nouveau système de définition (DSL), le renforcement de la sécurité et de l'isolation des environnements d'exécution, ainsi que l'amélioration de la visibilité sur la performance et les coûts via de nouveaux outils de supervision.

### Évolutions fonctionnelles
- **Bots & Agents**
  - Lancement de `gitops-warden 0.2.0` incluant des verdicts en français, le rendu Helm et des liens de suivi de run ([#2389](https://github.com/SocialGouv/iterion/issues/2389)).
  - Mise à jour majeure de l'agent d'accessibilité `Acci` (v3) basée sur le moteur ultra11y ([#2387](https://github.com/SocialGouv/iterion/issues/2387)).
  - Amélioration de la surveillance de production avec le système `Argus` (intégration des flux Sentry et Loki) ([#1869](https://github.com/SocialGouv/iterion/issues/1869), [#1702](https://github.com/SocialGouv/iterion/issues/1702)).
- **Interface Studio & Administration**
  - Ajout de nouveaux écrans d'administration pour la gestion des rôles des bots, des environnements sandbox, et du suivi de la consommation des crédits ([#1443](https://github.com/SocialGouv/iterion/issues/1443), [#1445](https://github.com/SocialGouv/iterion/issues/1445), [#1442](https://github.com/SocialGouv/iterion/issues/1442)).
  - Optimisation de la console d'administration avec une navigation par sections et une meilleure gestion des hiérarchies d'organisation ([#2365](https://github.com/SocialGouv/iterion/issues/2365)).
  - Nouvelle vue "Source" par fichier dans le Studio pour une meilleure inspection du code ([#1738](https://github.com/SocialGouv/iterion/issues/1738)).
- **Gestion des modèles LLM**
  - Introduction d'une politique de routage adaptatif permettant de gérer les modèles par niveau (organisation, équipe, bot) ([#2110](https://github.com/SocialGouv/iterion/issues/2110), [#2126](https://github.com/SocialGouv/iterion/issues/2126)).
  - Mise en place de politiques de repli (fallback) personnalisables pour les fournisseurs de modèles ([#2309](https://github.com/SocialGouv/iterion/issues/2309)).

### Évolutions techniques
- **Langage de définition (DSL)**
  - Refonte majeure du DSL (projet "Author YAML twin") pour améliorer la validation, le formatage et la gestion des commentaires lors de l'écriture des workflows ([#1720](https://github.com/SocialGouv/iterion/issues/1720), [#1664](https://github.com/SocialGouv/iterion/issues/1664), [#1344](https://github.com/SocialGouv/iterion/issues/1344)).
  - Renforcement de la validation des variables et des contraintes dès la phase de lancement ([#2329](https://github.com/SocialGouv/iterion/issues/2329)).
- **Infrastructure & Cloud**
  - Déploiement de "Sovereign Runner Pools" pour garantir une isolation stricte des ressources par pool ([#2273](https://github.com/SocialGouv/iterion/issues/2273)).
  - Intégration de SeaweedFS comme magasin d'objets pour l'environnement de développement ([#1943](https://github.com/SocialGouv/iterion/issues/1943)).
- **Sécurité & Isolation**
  - Implémentation du "Sovereign Sealing" pour sécuriser les secrets et l'identité des processus au sein des pools ([#2236](https://github.com/SocialGouv/iterion/issues/2236)).
  - Durcissement de l'isolation des sandboxes (refus des liens symboliques, protection des variables d'environnement de l'hôte) ([#2360](https://github.com/SocialGouv/iterion/issues/2360), [#2325](https://github.com/SocialGouv/iterion/issues/2325)).
- **Runtime & Performance**
  - Optimisation de l'attribution des coûts et du suivi des jetons (tokens) par tâche ([#2255](https://github.com/SocialGouv/iterion/issues/2255), [#2241](https://github.com/SocialGouv/iterion/issues/2241)).
  - Amélioration de la résilience des exécutions via une gestion plus robuste de la reprise (resume) de sessions ([#2332](https://github.com/SocialGouv/iterion/issues/2332), [#1490](https://github.com/SocialGouv/iterion/issues/1490)).

### Autres changements
- **Documentation** : Mise à jour importante de la documentation technique, notamment sur le nouveau DSL et la structure des domaines d'agents ([#1342](https://github.com/SocialGouv/iterion/issues/1342), [#2106](https://github.com/SocialGouv/iterion/issues/2106)).
- **Nettoyage** : Suppression de plusieurs composants et fonctions obsolètes (legacy) pour alléger le système ([#2298](https://github.com/SocialGouv/iterion/issues/2298)).

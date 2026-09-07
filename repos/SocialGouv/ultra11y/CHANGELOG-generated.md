## Changelog : ultra11y (30 derniers jours, au 06/09/2026)

### Résumé
Cette période a été marquée par une montée en puissance de la précision des audits et de la granularité des rapports. Les évolutions majeures concernent l'amélioration de l'intelligence artificielle pour l'arbitrage des critères d'accessibilité, ainsi que l'introduction de rapports détaillés par page. L'outil est désormais plus robuste dans ses environnements d'intégration continue (CI), offrant une meilleure gestion des coûts et des ressources lors des analyses complexes.

### Évolutions fonctionnelles
- **Amélioration du reporting :**
  - Publication de rapports de statut compacts par page pour une lecture rapide dans les flux de CI.
  - Regroupement des non-conformités par critère dans les commentaires de Pull Request pour faciliter les corrections.
  - Mise à jour du tableau de bord pour assurer une cohérence parfaite avec les rapports d'exécution.
  - Publication du taux de conformité basé sur le référentiel officiel plutôt que sur les capacités brutes du moteur.
- **Gestion des standards :**
  - Sélection globale du standard (WCAG ou RGAA) qui s'applique désormais de manière cohérente à l'ensemble des commandes de l'outil.
  - Extension de la couverture déterministe pour les critères du RGAA.

### Évolutions techniques
- **Intelligence Artificielle & Arbitrage (Adjudication) :**
  - Optimisation de la gestion des budgets de jetons (tokens) et des échecs de modèles pour éviter l'interruption complète des audits.
  - Amélioration de la logique de raisonnement de l'agent pour mieux traiter les cas d'incertitude et les refus de critères.
  - Refactorisation du moteur d'arbitrage pour le rendre agnostique au mode de transport des données.
  - Meilleure distinction et gestion entre les différents niveaux de service (tiers API vs tiers Agent).
- **CI/CD & Automatisation :**
  - Création d'un nouveau canal (lane) de Pull Request dédié aux tests RGAA déterministes.
  - Optimisation des workflows GitHub Actions, incluant la mise en cache des navigateurs Playwright et une meilleure gestion du "browser tier".
  - Amélioration de l'efficacité des audits via un système de "ledger" permettant le rejeu des résultats validés.
- **Moteur d'audit & Sondes (Probes) :**
  - Renforcement des sondes de détection pour éviter les faux positifs sur les indicateurs de focus et les pièges au clavier.
  - Amélioration du crawler pour une meilleure gestion des erreurs de pages (404) et des adresses multiples.
  - Optimisation du moteur de scan pour permettre des mesures plus précises sur les éléments animés.

### Autres changements
- Mise à jour régulière des sources de référence pour les standards WCAG et RGAA.
- Nettoyage de la documentation technique et des fichiers de configuration.
- Optimisation de la taille des artefacts produits lors des rapports compacts.

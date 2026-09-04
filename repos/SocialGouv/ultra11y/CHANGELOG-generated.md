## Changelog : ultra11y (30 derniers jours, au 3 septembre 2026)

### Résumé
Ce mois-ci, ultra11y a franchi une étape majeure dans la précision et la fiabilité de ses audits d'accessibilité. Les utilisateurs bénéficient désormais de rapports beaucoup plus détaillés, avec une visibilité accrue par page et par critère. En coulisses, l'utilisation de l'intelligence artificielle a été optimisée pour être plus robuste et économique, tandis que l'intégration continue (CI) a été considérablement renforcée pour permettre des tests plus profonds grâce à l'introduction d'un mode "navigateur" intégré.

### Évolutions fonctionnelles
- **Amélioration de la visibilité des résultats** : les rapports publient désormais le taux de conformité officiel du référentiel (RGAA/WCAG) et proposent des vues compactes par page pour une lecture rapide dans les flux de travail.
- **Regroupement intelligent des erreurs** : les non-conformités sont désormais regroupées par critère dans les commentaires de Pull Request, facilitant ainsi le travail de correction des développeurs.
- **Précision accrue du diagnostic** : meilleure gestion des critères "Non Applicable" et possibilité de sélectionner un référentiel (RGAA ou WCAG) de manière globale pour l'ensemble de l'audit.
- **Nouvelles mesures** : ajout de la capacité de mesurer le critère 2.4.11.

### Évolutions techniques
- **Optimisation de l'adjudication par IA** : 
    - Introduction de différents "tiers" (API, Agent, Browser) pour moduler la profondeur de l'audit et le coût associé.
    - Amélioration de la gestion des budgets de jetons (tokens) et de l'effort de raisonnement des modèles (Claude).
    - Refactoring du moteur pour rendre l'adjudication indépendante du mode de transport des données.
- **Renforcement de la CI/CD** :
    - Intégration d'un "browser tier" complet directement dans la GitHub Action ([#31](https://github.com/SocialGouv/ultra11y/pull/31)).
    - Mise en place de "keyed passes" pour permettre des exécutions ciblées et plus efficaces ([#28](https://github.com/SocialGouv/ultra11y/pull/28)).
    - Optimisation des performances via la mise en cache des navigateurs Playwright et la réduction de la taille des artefacts de rapport.
- **Fiabilisation du moteur de scan** :
    - Amélioration du crawling pour mieux gérer les URLs canoniques ([#27](https://github.com/SocialGouv/ultra11y/pull/27)) et les erreurs 404 ([#26](https://github.com/SocialGouv/ultra11y/pull/26)).
    - Mise à jour régulière des sources de référence (WCAG et RGAA) intégrées au moteur.

### Autres changements
- **Documentation** : mise à jour du README et des guides techniques concernant la couverture déterministe, les commandes de la CI et l'utilisation des "skills".
- **Nettoyage** : suppression de fichiers de configuration obsolètes et optimisation du processus de build.

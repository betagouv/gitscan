## Changelog : sante-mentale-etudiant (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'accessibilité numérique, la conformité légale et l'amélioration de la clarté du contenu. Le site a bénéficié d'une mise en conformité majeure avec les standards d'accessibilité, de l'ajout de transcriptions pour les contenus multimédias et de la mise en place de pages légales essentielles. L'expérience utilisateur a également été affinée grâce à des mises à jour textuelles importantes et une interface plus cohérente.

### Évolutions fonctionnelles
- **Accessibilité et inclusion**
  - Amélioration globale de l'accessibilité (gestion du focus, liens de saut, conformité aux validateurs W3) sur l'ensemble des pages clés [#94](https://github.com/betagouv/sante-mentale-etudiant/pull/94), [#101](https://github.com/betagouv/sante-mentale-etudiant/pull/101), [#104](https://github.com/betagouv/sante-mentale-etudiant/pull/104).
  - Mise à jour de la déclaration d'accessibilité du site [#66](https://github.com/betagouv/sante-mentale-etudiant/pull/66).
  - Ajout de transcriptions textuelles pour les vidéos et les podcasts afin de faciliter l'accès aux contenus [#65](https://github.com/betagouv/sante-mentale-etudiant/pull/65), [#71](https://github.com/betagouv/sante-mentale-etudiant/pull/71).
- **Contenu et information**
  - Intégration de nouveaux avertissements (disclaimers) sur les pages sensibles (ressenti, conseils, s'informer) pour mieux encadrer l'usage des ressources [#80](https://github.com/betagouv/sante-mentale-etudiant/pull/80), [#87](https://github.com/betagouv/sante-mentale-etudiant/pull/87), [#114](https://github.com/betagouv/sante-mentale-etudiant/pull/114).
  - Publication des pages de mentions légales et de politique de confidentialité [#82](https://github.com/betagouv/sante-mentale-etudiant/pull/82), [#83](https://github.com/betagouv/sante-mentale-etudiant/pull/83).
  - Enrichissement du catalogue : nouveaux articles, nouvelles vidéos (SPE/Nightline) et mise à jour des statistiques de la page d'accueil [#68](https://github.com/betagouv/sante-mentale-etudiant/pull/68), [#88](https://github.com/betagouv/sante-mentale-etudiant/pull/88).
- **Expérience utilisateur (UX/UI)**
  - Refonte visuelle incluant un nouveau logo [#123](https://github.com/betagouv/sante-mentale-etudiant/pull/123) et une nouvelle page d'erreur 404 [#103](https://github.com/betagouv/sante-mentale-etudiant/pull/103).
  - Optimisation de la recherche de soutien : affichage de cartes d'aide spécifiques en cas d'absence de résultats [#116](https://github.com/betagouv/sante-mentale-etudiant/pull/116).
  - Simplification de l'interface par la suppression de la gestion des cookies [#97](https://github.com/betagouv/sante-mentale-etudiant/pull/97).

### Évolutions techniques
- **Référencement et performance**
  - Mise en place d'un sitemap et optimisation des métadonnées pour améliorer le référencement naturel (SEO) [#62](https://github.com/betagouv/sante-mentale-etudiant/pull/62), [#92](https://github.com/betagouv/sante-mentale-etudiant/pull/92).
  - Optimisation des assets par la conversion de formats d'images (PNG vers SVG) [#108](https://github.com/betagouv/sante-mentale-etudiant/pull/108).
- **Architecture et maintenance**
  - Mise à jour de l'environnement d'exécution vers Node.js 24.22.1 [#128](https://github.com/betagouv/sante-mentale-etudiant/pull/128).
  - Refactorisation du composant "disclaimer" pour une meilleure modularité [#87](https://github.com/betagouv/sante-mentale-etudiant/pull/87).
  - Nettoyage de la structure HTML (suppression de doublons de balises `<main>`) [#102](https://github.com/betagouv/sante-mentale-etudiant/pull/102).
  - Correction de la hiérarchie des titres (H1, H2, H3) pour respecter les standards sémantiques [#61](https://github.com/betagouv/sante-mentale-etudiant/pull/61).

### Autres changements
- Révision majeure de la rédaction (wording) sur l'ensemble du site pour garantir un ton adapté et bienveillant.
- Nettoyage de la base de données (suppression de champs inutiles dans les articles externes) [#107](https://github.com/betagouv/sante-mentale-etudiant/pull/107).

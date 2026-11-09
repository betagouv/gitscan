## Changelog : simplifions (30 derniers jours, au 6 novembre 2026)

### Résumé
Ce mois-ci, Simplifions a franchi une étape importante dans la maturité de son interface d'administration et de son catalogue public. L'accent a été mis sur la fluidité de la gestion des contenus (notamment via un meilleur suivi des brouillons), l'accessibilité du site et la précision de nos outils de mesure d'audience. L'expérience d'administration est désormais plus intuitive avec un nouveau tableau de bord et des outils de prévisualisation avant publication.

### Évolutions fonctionnelles

**Administration & Backoffice**
- Mise en place d'un nouveau tableau de bord pour les administrateurs, affichant les statistiques du catalogue, les dernières fiches modifiées et les brouillons en attente. [#232](https://github.com/datagouv/simplifions/issues/232)
- Amélioration majeure de la gestion des brouillons : visibilité accrue dans les listes, mentions spécifiques "Brouillon" et gestion plus fine du cycle de vie des fiches. [#204](https://github.com/datagouv/simplifions/issues/204), [#205](https://github.com/datagouv/simplifions/issues/205), [#206](https://github.com/datagouv/simplifions/issues/206)
- Nouvelle fonctionnalité de prévisualisation permettant de voir exactement ce qui sera publié avant de valider une fiche démarche. [#239](https://github.com/datagouv/simplifions/issues/239)
- Possibilité de réorganiser l'ordre des API fournies au sein d'une solution par simple glisser-déposer. [#210](https://github.com/datagouv/simplifions/issues/210)
- Refonte du menu d'administration pour une navigation plus claire en quatre entrées principales. [#229](https://github.com/datagouv/simplifions/issues/229)

**Catalogue & Expérience Utilisateur**
- Optimisation des pages "Cas d'usage" avec un meilleur affichage des sections et la possibilité de comparer les solutions dans un tableau. [#176](https://github.com/datagouv/simplifions/issues/176)
- Amélioration de la recherche : la recherche est désormais insensible à la casse et propose des messages clairs en cas d'absence de résultat. [#202](https://github.com/datagouv/simplifions/issues/202)
- Renforcement de l'accessibilité : amélioration de la navigation au clavier, support optimisé des lecteurs d'écran (annonce des changements de nombres) et meilleur contraste des éléments. [#170](https://github.com/datagouv/simplifions/issues/170), [#184](https://github.com/datagouv/simplifions/issues/184)
- Refonte de la page "Nous contacter" : intégration d'un fil d'Ariane, choix facilité du cas d'usage concerné et modèles de messages copiables. [#221](https://github.com/datagouv/simplifions/issues/221)
- Mise à jour du pied de page pour inclure des liens vers le catalogue, les guides et la page de contact. [#209](https://github.com/datagouv/simplifions/issues/209)
- Optimisation du SEO via la possibilité de saisir des titres spécifiques pour les moteurs de recherche. [#170](https://github.com/datagouv/simplifions/issues/170)

**Processus de revue**
- Amélioration de la boucle de revue de qualité : distinction plus nette entre les constats (risques) et les preuves (détails) pour faciliter la prise de décision. [#232](https://github.com/datagouv/simplifions/issues/232)

### Évolutions techniques

**Sécurité & Core**
- Mise à jour de sécurité de Rails (8.1.4.1) et de Rack (3.2.8) pour corriger plusieurs failles connues. [#224](https://github.com/datagouv/simplifions/issues/224), [#193](https://github.com/datagouv/simplifions/issues/193)
- Passage à Ruby 4.0.9.
- Correction de sécurité sur la dépendance `addressable`. [#196](https://github.com/datagouv/simplifions/issues/196)

**Analytics (Matomo)**
- Refonte complète du suivi Matomo : mesure précise des vues de pages (même via Turbo), des clics sortants, des recherches effectuées et des parcours spécifiques (contact, footer, types de solutions). [#211](https://github.com/datagouv/simplifions/issues/211), [#212](https://github.com/datagouv/simplifions/issues/212), [#225](https://github.com/datagouv/simplifions/issues/225)
- Configuration de Matomo via API pour une meilleure fiabilité des données. [#212](https://github.com/datagouv/simplifions/issues/212)

**Expérience Développeur (DX)**
- Amélioration significative du workflow de développement via `worktree`, permettant d'isoler chaque sujet de travail dans un environnement dédié (bases de données et ports distincts).
- Optimisation des processus automatisés de vérification des fonctionnalités ("Carte de vérif").

### Autres changements
- Mise à jour de la documentation interne (`REVIEW.md`, `CLAUDE.md`).
- Nettoyage du code et suppression de dépendances inutilisées (PWA, etc.).

## Changelog : aides-agri (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois, la plateforme a franchi des étapes importantes pour mieux servir les agriculteurs, notamment avec l'introduction de notifications par email, une gestion plus fine des aides locales et une navigation plus fluide. L'outil renforce également sa visibilité et son utilité grâce à l'amélioration de la cartographie et à l'ouverture de ses données via data.gouv.

### Évolutions fonctionnelles

**Nouvelles fonctionnalités**
- Mise en place de notifications par email pour informer les utilisateurs des nouvelles aides selon leurs critères [#743](https://github.com/betagouv/aides-agri/issues/743).
- Possibilité d'associer une aide à plusieurs organismes porteurs [#726](https://github.com/betagouv/aides-agri/issues/726).
- Amélioration de la recherche permettant de sélectionner l'ensemble des filières sur la page de résultats [#806](https://github.com/betagouv/aides-agri/issues/806).
- Meilleure gestion des spécificités locales des aides et optimisation du choix du département [#841](https://github.com/betagouv/aides-agri/issues/841), [#838](https://github.com/betagouv/aides-agri/issues/838).
- Création d'une page "À propos" pour présenter la plateforme [#637](https://github.com/betagouv/aides-agri/issues/637).
- Clarification de la structure des fiches (distinction entre fiches mères et fiches minimales) [#851](https://github.com/betagouv/aides-agri/issues/851).

**Améliorations de l'expérience utilisateur (UX/UI)**
- Amélioration de la cartographie de déploiement des aides [#844](https://github.com/betagouv/aides-agri/issues/844), [#824](https://github.com/betagouv/aides-agri/issues/824).
- Optimisation de la lisibilité des tableaux larges [#827](https://github.com/betagouv/aides-agri/issues/827) et de l'affichage de la page de résultats [#825](https://github.com/betagouv/aides-agri/issues/825).
- Engagement pour l'amélioration continue de l'accessibilité [#807](https://github.com/betagouv/aides-agri/issues/807).
- Correction de divers bugs d'affichage (CSS manquant [#848](https://github.com/betagouv/aides-agri/issues/848), page d'aide [#797](https://github.com/betagouv/aides-agri/issues/797)) et du composant de sélection multiple [#826](https://github.com/betagouv/aides-agri/issues/826).
- Correction des liens externes dans les emails d'alerte [#862](https://github.com/betagouv/aides-agri/issues/862).
- Mise à jour de la terminologie : "date de mise à jour" devient "date de vérification" [#793](https://github.com/betagouv/aides-agri/issues/793).

**Administration et données**
- Ajout de statistiques simples directement dans l'interface d'administration [#847](https://github.com/betagouv/aides-agri/issues/847).
- Mise à jour des statistiques de la plateforme pour septembre 2026 [#861](https://github.com/betagouv/aides-agri/issues/861).

### Évolutions techniques

**Backend et infrastructure**
- Résolution de problèmes liés aux réglages de l'application Django [#787](https://github.com/betagouv/aides-agri/issues/787), [#788](https://github.com/betagouv/aides-agri/issues/788).

**Analyse et outils**
- Mise en place de la mesure d'actions utilisateurs sur la page de résultats pour améliorer l'analyse de l'usage [#823](https://github.com/betagouv/aides-agri/issues/823).
- Développement d'un script pour la génération automatique de la carte de déploiement [#822](https://github.com/betagouv/aides-agri/issues/822).

### Autres changements

- Publication d'un jeu de données sur data.gouv pour permettre une exploitation facile via Excel [#809](https://github.com/betagouv/aides-agri/issues/809).
- Mise à jour du fichier de sécurité `security.txt` [#791](https://github.com/betagouv/aides-agri/issues/791).

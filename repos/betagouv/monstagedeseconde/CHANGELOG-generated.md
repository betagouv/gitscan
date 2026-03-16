## Changelog : monstagedeseconde (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution de MonStage. Les améliorations concernent principalement des corrections de bugs et des améliorations de la gestion des offres de stage et des établissements scolaires. Des scripts d'importation ont été améliorés et des corrections ont été apportées aux emails et aux notifications. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct des conventions pour les gestionnaires d'établissement scolaire. [#752](https://github.com/betagouv/monstagedeseconde/pulls/752)
- Amélioration de la fonction de signalement des offres inappropriées. [#770](https://github.com/betagouv/monstagedeseconde/pulls/770)
- Correction d'un bug empêchant l'affichage correct d'une seule convention pour un élève. [#1580](https://github.com/betagouv/monstagedeseconde/issues/1580)
- Correction d'un bug lié aux établissements scolaires sans département associé. [#1579](https://github.com/betagouv/monstagedeseconde/issues/1579)
- Correction d'un bug lié aux membres sans zone géographique associée. [#1581](https://github.com/betagouv/monstagedeseconde/issues/1581)
- Amélioration de l'affichage des offres de stage pour les collèges et lycées. [#756](https://github.com/betagouv/monstagedeseconde/pulls/756)
- Ajout d'une notification par email pour le lancement des signatures de conventions. [#771](https://github.com/betagouv/monstagedeseconde/pulls/771)
- Correction du captcha [#1584](https://github.com/betagouv/monstagedeseconde/pulls/1584)
- Correction du code postal de la réunion [#760](https://github.com/betagouv/monstagedeseconde/pulls/760)

### Évolutions techniques
- Amélioration de la gestion des erreurs lors de l'analyse JSON dans le contrôleur `ApiEntrepriseProxyController`. [#776](https://github.com/betagouv/monstagedeseconde/pulls/776)
- Correction d'une erreur `ActiveModel::MissingAttributeError` dans la gestion des utilisateurs et des établissements scolaires. [#778](https://github.com/betagouv/monstagedeseconde/pulls/778)
- Amélioration du script de duplication des offres de stage pour gérer les erreurs et les offres non valides. [#772](https://github.com/betagouv/monstagedeseconde/pulls/772)
- Mise à jour de plusieurs dépendances :
    - `nokogiri` de 1.19.0 à 1.19.1 [#767](https://github.com/betagouv/monstagedeseconde/pulls/767)
    - `immutable` de 5.1.4 à 5.1.5 [#767](https://github.com/betagouv/monstagedeseconde/pulls/767)
    - `qs` de 6.14.1 à 6.14.2 [#767](https://github.com/betagouv/monstagedeseconde/pulls/767)
    - `faraday` de 2.14.0 à 2.14.1 [#769](https://github.com/betagouv/monstagedeseconde/pulls/769)
    - `rack` de 3.2.4 à 3.2.5 [#769](https://github.com/betagouv/monstagedeseconde/pulls/769)
- Amélioration de la configuration Ruby LSP.

### Autres changements
- Ajout de la gem `letter_thief`. [#750](https://github.com/betagouv/monstagedeseconde/pulls/750)
- Amélioration de la documentation et des tests unitaires.
- Corrections de typographie et d'accents.
- Nettoyage du code et refactoring de certaines parties de l'application.
- Mise à jour des paramètres de production dans la base de données.
- Amélioration des scripts d'importation des établissements scolaires.

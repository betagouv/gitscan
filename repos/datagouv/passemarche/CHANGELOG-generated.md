## Changelog : passemarche (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du parcours candidat, notamment l'accès aux candidatures depuis un tableau de bord, la gestion des lots et l'affichage des informations. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Tableau de bord candidat :** Ajout d'un tableau de bord permettant aux candidats d'accéder à leurs candidatures. Un bandeau bleu informe de la disponibilité de cette nouvelle fonctionnalité. [#364](https://github.com/datagouv/passemarche/pull/364)
- **Consultation des candidatures :** Possibilité pour les candidats de consulter le détail de leurs candidatures. [#371](https://github.com/datagouv/passemarche/pull/371)
- **Gestion des lots :** Amélioration du parcours candidat avec les lots, notamment la séparation de l'identification de l'entreprise et la sélection des lots. Correction d'un problème de soumission multiple. [#351](https://github.com/datagouv/passemarche/pull/351), [#363](https://github.com/datagouv/passemarche/pull/363), [#372](https://github.com/datagouv/passemarche/pull/372)
- **Affichage des types de lots :** Affichage des types de lots reçus de la plateforme d'achat. [#383](https://github.com/datagouv/passemarche/pull/383)
- **Suppression d'une candidature :** Ajout de la fonctionnalité permettant de supprimer une candidature. [#377](https://github.com/datagouv/passemarche/pull/377)
- **URLs de retour :** Configuration des URLs de retour pour l'acheteur et le candidat. [#378](https://github.com/datagouv/passemarche/pull/378)
- **Informations sur l'acheteur :** Affichage du nom de l'acheteur dans le tableau de bord candidat. [#365](https://github.com/datagouv/passemarche/pull/365)
- **Raison sociale INSEE :** Récupération de la raison sociale de l'acheteur depuis l'INSEE après la création du marché. [#365](https://github.com/datagouv/passemarche/pull/365)
- **Amélioration de l'attestation candidat :** Ajustements de l'interface utilisateur et du libellé pour l'attestation candidat, notamment pour plusieurs lots. [#391](https://github.com/datagouv/passemarche/pull/391), [#382](https://github.com/datagouv/passemarche/pull/382)

### Évolutions techniques
- **Refactoring de l'authentification candidat :** Refactorisation de l'authentification candidat pour améliorer la gestion de session. [#376](https://github.com/datagouv/passemarche/pull/376)
- **Optimisation des presenters :** Optimisation des presenters pour améliorer la performance et la lisibilité du code. [#355](https://github.com/datagouv/passemarche/pull/355)
- **Correction de la validation CPV :** Correction d'un problème de validation des codes CPV. [#361](https://github.com/datagouv/passemarche/pull/361)

### Autres changements
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (bootsnap, devise, jbuilder, pagy, puma, rubyzip, selenium-webdriver, view_component).
- **Ajout de tests :** Ajout de tests RSpec, Cucumber et FactoryBot pour les nouvelles fonctionnalités et corrections.
- **Documentation :** Ajout de traductions pour l'annexe des lots.
- **Configuration :** Ajout des clés Brevo pour la production. [#367](https://github.com/datagouv/passemarche/pull/367)
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Ajout de raccourcis SIRET cliquables :** Ajout de raccourcis SIRET cliquables dans l'éditeur de test. [#368](https://github.com/datagouv/passemarche/pull/368)

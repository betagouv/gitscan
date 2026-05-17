## Changelog : passemarche (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du parcours de candidature pour les entreprises, notamment la gestion des lots et l'accès au tableau de bord candidat. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Tableau de bord candidat :** Ajout d'un tableau de bord pour les candidats, permettant de consulter leurs candidatures et d'accéder à une synthèse de leurs informations. Une bannière d'information est également affichée. [#364](https://github.com/datagouv/passemarche/pull/364)
- **Consultation des candidatures :** Possibilité pour les candidats de consulter le détail de leurs candidatures. [#371](https://github.com/datagouv/passemarche/pull/371)
- **Gestion des lots :** Amélioration du parcours de sélection des lots pour les candidats, avec affichage de la progression et possibilité de soumettre directement la candidature.  Plusieurs correctifs et refactorisations ont été apportés pour gérer les cas avec plusieurs lots et un seul type de code CPV. [#346](https://github.com/datagouv/passemarche/pull/346), [#350](https://github.com/datagouv/passemarche/pull/350), [#352](https://github.com/datagouv/passemarche/pull/352), [#362](https://github.com/datagouv/passemarche/pull/362), [#363](https://github.com/datagouv/passemarche/pull/363)
- **Informations acheteur :** Affichage du nom du raison sociale de l'acheteur dans le tableau de bord candidat.  Récupération de cette information via l'INSEE. [#365](https://github.com/datagouv/passemarche/pull/365)
- **URLs de retour :** Configuration des URLs de retour pour l'acheteur et le candidat après authentification.  Ajout de tests associés. [#378](https://github.com/datagouv/passemarche/pull/378)

### Évolutions techniques
- **Refactoring de l'authentification candidat :** Simplification et amélioration de la gestion de l'authentification des candidats. [#376](https://github.com/datagouv/passemarche/pull/376)
- **Unification des presenters :** Regroupement des méthodes communes des presenters pour améliorer la maintenabilité. [#375](https://github.com/datagouv/passemarche/pull/375)
- **Amélioration des tests :** Ajout de tests Cucumber pour les pages de synchronisation et le nouveau parcours candidat avec lots. [#374](https://github.com/datagouv/passemarche/pull/374)
- **Optimisation des presenters :** Amélioration des performances des presenters en utilisant la mémoïsation et en évitant les appels directs aux modèles dans les vues. [#355](https://github.com/datagouv/passemarche/pull/355)
- **Gestion des webhooks :** Déplacement de l'enfilement des webhooks dans un organisateur dédié.
- **Correction de validation CPV :** Correction d'un problème de validation des codes CPV. [#361](https://github.com/datagouv/passemarche/pull/361)

### Autres changements
- Mise à jour des dépendances : Bootsnap, View Component, Devise, Puma, Propshaft, Pagy.
- Ajout de raccourcis cliquables pour les SIRET dans l'éditeur de test. [#368](https://github.com/datagouv/passemarche/pull/368)
- Ajout des clés Brevo pour la production. [#367](https://github.com/datagouv/passemarche/pull/367)
- Ajout de scopes pour le tableau de bord candidat à MarketApplication.

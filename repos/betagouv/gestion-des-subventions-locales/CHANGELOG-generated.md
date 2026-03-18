## Changelog : gestion-des-subventions-locales (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, de la performance et de l'expérience utilisateur. Des correctifs ont été apportés pour la gestion des données, l'import depuis DN, et l'affichage des tableaux. L'ajout de l'authentification à deux facteurs pour les utilisateurs staff renforce la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour les utilisateurs staff [#537](https://github.com/betagouv/gestion-des-subventions-locales/pull/537).
- Possibilité de renommer les simulations [#568](https://github.com/betagouv/gestion-des-subventions-locales/pull/568).
- Ajout de pages Mentions légales et Données personnelles [#571](https://github.com/betagouv/gestion-des-subventions-locales/pull/571).
- Ajout d'une page listant les projets avec des annotations manquantes sur DN [#555](https://github.com/betagouv/gestion-des-subventions-locales/pull/555).
- Possibilité de modifier les données d'un dossier via l'interface d'administration.
- Ajout de colonnes "Commentaires" et "Champs libres" dans les tableaux [#563](https://github.com/betagouv/gestion-des-subventions-locales/pull/563).
- Ajout de la colonne "N° D.N." avec lien vers D.N. dans les tableaux [#548](https://github.com/betagouv/gestion-des-subventions-locales/pull/548).
- Correction de l'affichage des taux avec le bon nombre de décimales [#557](https://github.com/betagouv/gestion-des-subventions-locales/pull/557).
- Correction de la persistance de la visibilité des colonnes masquées par défaut [#564](https://github.com/betagouv/gestion-des-subventions-locales/pull/564).

### Évolutions techniques
- Activation du cache-busting pour les fichiers statiques [#589](https://github.com/betagouv/gestion-des-subventions-locales/pull/589).
- Synchronisation incrémentale des dossiers DN par curseur [#579](https://github.com/betagouv/gestion-des-subventions-locales/pull/579).
- Mise en place d'événements Matomo pour le suivi analytique [#581](https://github.com/betagouv/gestion-des-subventions-locales/pull/581).
- Refactorisation de l'édition inline des simulations avec des Class-Based Views (CBV) et des formulaires DSFR [#576](https://github.com/betagouv/gestion-des-subventions-locales/pull/576).
- Migration des tableaux vers la structure DSFR et application du nommage BEM [#544](https://github.com/betagouv/gestion-des-subventions-locales/pull/544).
- Ajout d'un scan antivirus ClamAV pour les logos des modèles et les documents uploadés [#525](https://github.com/betagouv/gestion-des-subventions-locales/pull/525).
- Ajout d'une tâche pour rafraîchir les dossiers de toutes les démarches depuis DN [#538](https://github.com/betagouv/gestion-des-subventions-locales/pull/538).
- Ajout d'une tâche pour rafraîchir les dossiers d'une démarche depuis une date donnée [#533](https://github.com/betagouv/gestion-des-subventions-locales/pull/533).
- Amélioration du style des filtres [#587](https://github.com/betagouv/gestion-des-subventions-locales/pull/587).

### Autres changements
- Ajout d'une vidéo de démo sur la page d'aide [#526](https://github.com/betagouv/gestion-des-subventions-locales/pull/526).
- Correction des pages d'erreur 403, 404 et 500 pour qu'elles soient conformes au modèle DSFR [#528](https://github.com/betagouv/gestion-des-subventions-locales/pull/528).
- Suppression de code mort (processModal.js) [#534](https://github.com/betagouv/gestion-des-subventions-locales/pull/534).
- Correction de divers bugs et améliorations de la stabilité.
- Suppression des warnings de django-axes [#584](https://github.com/betagouv/gestion-des-subventions-locales/pull/584).
- Ajout d'un bouton de réinitialisation des colonnes [#565](https://github.com/betagouv/gestion-des-subventions-locales/pull/565).
- Correction de la notification pour un projet accepté [#578](https://github.com/betagouv/gestion-des-subventions-locales/pull/578).
- Ajout d'un paramètre pour relancer une tâche [#580](https://github.com/betagouv/gestion-des-subventions-locales/pull/580).
- Correction de l'export CSV pour afficher les nombres décimaux avec une virgule [#577](https://github.com/betagouv/gestion-des-subventions-locales/pull/577).
- Correction de la mise en page du dropdown de visibilité des colonnes [#583](https://github.com/betagouv/gestion-des-subventions-locales/pull/583).
- Correction du style du bouton de confirmation de suppression d'une enveloppe [#586](https://github.com/betagouv/gestion-des-subventions-locales/pull/586).
- Correction des bordures du tableau d'enveloppes et ajout de marge [#573](https://github.com/betagouv/gestion-des-subventions-locales/pull/573).
- Ajout de la possibilité de configurer un ID Matomo spécifique pour l'environnement de staging [#532](https://github.com/betagouv/gestion-des-subventions-locales/pull/532).
- Correction d'un problème de scroll lié au bloc enveloppe [#558](https://github.com/betagouv/gestion-des-subventions-locales/pull/558).
- Ajout d'une protection contre les attaques par force brute [#524](https://github.com/betagouv/gestion-des-subventions-locales/pull/524).
- Correction de l'import d'un dossier qui ne s'interrompait pas en cas d'erreur sur un champ [#574](https://github.com/betagouv/gestion-des-subventions-locales/pull/574).
- Correction d'un problème de récupération des catégories DETR pour les territoires non gérés [#552](https://github.com/betagouv/gestion-des-subventions-locales/pull/552).
- Ajout d'une limite de 3 lignes maximum pour les cellules du tableau [#553](https://github.com/betagouv/gestion-des-subventions-locales/pull/553).
- Correction d'un bug empêchant la suppression de projets via l'admin.
- Ajout de droits pour les utilisateurs "équipe" pour modifier les périmètres des autres utilisateurs [#531](https://github.com/betagouv/gestion-des-subventions-locales/pull/531).
- Correction de l'export des noms de colonnes [#580](https://github.com/betagouv/gestion-des-subventions-locales/pull/580).
- Ajout de la possibilité de ne pas interrompre l'import d'un dossier en cas d'erreur sur un champ [#561](https://github.com/betagouv/gestion-des-subventions-locales/pull/561).
- Ajout d'un trigger `merge_group` au workflow CI [#572](https://github.com/betagouv/gestion-des-subventions-locales/pull/572).
- Correction du dropdown de colonnes en mode sombre [#570](https://github.com/betagouv/gestion-des-subventions-locales/pull/570).
- Correction de tests et ajout de tests manquants.
- Diverses corrections de style et améliorations de la lisibilité du code.

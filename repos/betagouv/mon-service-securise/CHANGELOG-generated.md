## Changelog : mon-service-securise (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'interface utilisateur avec l'intégration du Design System de la République Française (DSFR), l'amélioration de l'expérience utilisateur autour du parcours d'homologation, et l'ajout de nouvelles fonctionnalités comme la gestion des administrateurs et l'affichage de l'indice cyber. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Intégration du Design System de la République Française (DSFR) pour l'en-tête et les composants d'interface.
- Refonte de la page "Sécuriser" avec l'ajout de l'indice cyber et des risques.
- Implémentation d'un parcours d'homologation en SPA (Single Page Application) avec gestion des étapes, des actions et de la navigation.
- Ajout de la gestion des administrateurs : attribution des droits, affichage dans l'interface et rattachement aux services.
- Ajout de la fonctionnalité de téléchargement du tampon d'homologation.
- Amélioration de l'affichage des dossiers d'homologation et ajout d'un bouton pour en créer ou en reprendre un.
- Ajout de nouvelles pages de destination pour "Sécurisez votre service numérique" et "Industrialisez vos homologations".
- Ajout d'un bloc "Communauté" sur la page d'accueil.

### Évolutions techniques
- Conversion de plusieurs modules (supervision, utilisateur) en TypeScript pour une meilleure maintenabilité.
- Refactorisation du code pour utiliser des composants Svelte plus simples.
- Amélioration de la structure du code et extraction de méthodes privées.
- Mise à jour des dépendances (vitest, typescript, eslint, etc.).
- Ajout de tests d'accessibilité avec Playwright et Axe.
- Utilisation de la nouvelle SPA pour la visite guidée.
- Suppression des anciennes vues `pug`.
- Amélioration des workflows de déploiement Clever Cloud.

### Autres changements
- Correction de typos et amélioration de la documentation.
- Suppression de fichiers inutiles.
- Amélioration des messages d'erreur et des retours d'information à l'utilisateur.
- Ajout de logs et de métriques pour faciliter le débogage et le suivi des performances.
- Correction de problèmes d'accessibilité.
- Correction de bugs divers liés à l'affichage et au fonctionnement de l'application.
- Correction d'une erreur `effect_update_depth_exceeded` sur la sélection du domaine de spécialité.
- Correction d'un problème de 404 sur les pages risques v2 et création de compte.
- Correction de l'affichage des badges d'homologation sur le tableau de bord.
- Correction de l'affichage du header en mode connecté.
- Correction du sticky des boutons d'actions.
- Correction du tableau de supervision.
- Correction de l'affichage des contacts utiles.
- Correction des tests du routeur.
- Correction des erreurs d'accessibilité.
- Suppression du bandeau de promotion de MSC.
- Ajout de tests d'accessibilité pour les pages publiques et la visite guidée.
- Publication des rapports de tests d'accessibilité au format markdown.
- Ajout de la possibilité de télécharger les screenshots des tests d'accessibilité.
- Ajout d'un retry sur la recherche d'entreprise.
- Ajout de la publication des rapports d'accessibilité dans Mattermost.
- Ajout de la possibilité de créer un utilisateur et un service dans le global setup des tests d'accessibilité.
- Suppression du brouillon de service créé à la fin des tests d'accessibilité.
- Correction d'une erreur sur le clic en dehors.
- Correction d'une erreur `o.elements.includes is not a function`.
- Correction de la possibilité d'accéder aux risques pour les utilisateurs n'ayant pas les droits d'accès.
- Correction de l'affichage de la page service si l'appel à `rafraichisServiceComplet` est terminé.
- Correction de l'affichage de l'indice cyber dans l'entête de page service si l'utilisateur n'a pas les droits d'accès.
- Correction de la suppression et de la création si les droits l'interdisent.
- Correction de l'affichage de la pastille dans les titres d'onglets.
- Correction du calcul de l'étape à afficher en fonction de l'URL.
- Correction de la sauvegarde de l'autorité d'homologation.
- Correction de l'affichage de la modale de démarche indicative.
- Correction de l'affichage de la page service dans le nouveau header.
- Correction de l'identifiant de la page `contactsUtiles`.
- Correction des tests du routeur.
- Correction de l'affichage des données du service complet.
- Correction de l'affichage des rubriques visibles.
- Correction de l'affichage du bandeau de simulation vers le référentiel V2.
- Correction de l'affichage des actions quand elles sont vides.
- Correction de la gestion des rubriques visibles au sein du routeur.
- Correction de l'affichage des contacts utiles du service depuis la représentation JSON du service complet.
- Correction de l'affichage du bouton de téléchargement du tampon d'homologation.
- Correction de l'affichage des dossiers d'homologation lorsqu'ils sont vides.
- Correction de l'affichage des valeurs d'indice cyber ANSSI et personnalisé dans la pastille des onglets.
- Correction de l'extraction de la méthode d'analyse de page.
- Correction de l'utilisation de `<Modale>`.
- Correction de l'utilisation de `<Pastille>`.
- Correction de l'utilisation de `<TitreOngletDSFR>`.
- Correction de l'utilisation de `<CarteFormulaire>`.
- Correction de l'utilisation de `<dsfr-link>`.
- Correction de l'utilisation de `<dsfr-dropdown>`.
- Correction de l'utilisation des slots du dsfr header.
- Correction de l'utilisation du texte dans le logo par les propriétés brad/tagline du dsfr-header.
- Correction de l'utilisation du dsfr-header.
- Correction de l'adaptation du contenu de la navigation pour le header.
- Correction de l'ajout du header DSFR.
- Correction de l'ajout du nom, prénom et email de l'utilisateur connecté à `reponse.locals`.
- Correction de l'ajout de la navigation principale par le composant `dsfr-navigation`.
- Correction de l'ajout de la page Indice Cyber dans la SPA.
- Correction de l'ajout de la navigation horizontale dans "SÉCURISER".
- Correction de l'ajout des risques V1 à la SPA.
- Correction de l'ajout des risques V1 à l'objet JSON de service complet.
- Correction de l'ajout du contenu du composant de page Contact utiles.
- Correction de l'ajout de la représentation JSON des contacts utiles à l'API du service complet.
- Correction de l'ajout de l'étape "Récapitulatif" au parcours homologation en SPA.
- Correction de l'ajout de l'étape "Téléchargement du dossier" au parcours homologation en SPA.
- Correction de l'ajout de l'étape "Documents" au parcours homologation en SPA.
- Correction de l'ajout de l'étape "Avis" au parcours homologation en SPA.
- Correction de l'ajout de l'étape "Décision" au parcours homologation en SPA.
- Correction de l'ajout de l'étapier du parcours d'homologation.
- Correction de l'ajout de la navigation au sein du parcours d'homologation.
- Correction de l'ajout du bouton "Précédent" pour naviguer dans le parcours.
- Correction de l'ajout du bouton "Suivant" pour naviguer dans le parcours.

## Changelog : gestion-des-subventions-locales (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des notifications, notamment la génération de documents en masse, et l'optimisation de la recherche et du filtrage des dossiers. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience globale. Des efforts ont été faits pour améliorer la robustesse et la performance du système, notamment en matière de synchronisation avec les sources de données externes.

### Évolutions fonctionnelles
- **Notifications :**
    - Possibilité de générer plusieurs documents (arrêtés et lettres) simultanément dans une modale dédiée. [#723, #727, #729]
    - Choix du format d'export (arrêtés, lettres, les deux) lors de la génération de documents.
    - Possibilité de définir le nom du fichier PDF lors de la génération de notifications d'acceptation. [#736]
    - Découplage de la notification de refus/classement du changement de statut pour plus de flexibilité. [#719]
    - Amélioration de la gestion des erreurs lors de la génération de documents.
    - Ajout d'une stratégie de remplacement pour les documents existants.
- **Recherche et Filtrage :**
    - Ajout d'un champ de recherche général sur les listes de projets, simulations et programmations, permettant de rechercher par intitulé, raison sociale et numéro de dossier. [#701]
    - Réordonnement du champ de recherche après l'utilisation du bouton de réinitialisation des filtres. [#702]
    - Amélioration de la gestion des filtres de type ModelMultipleChoiceFilter pour corriger un problème de décochage silencieux. [#737]
- **Gestion des dossiers :**
    - Possibilité de récupérer un dossier depuis DN via une action dédiée dans le back-office. [#696]
    - Désactivation des dossiers supprimés/archivés depuis DN pour éviter les incohérences. [#716]
    - Amélioration du formatage de l'adresse du demandeur dans les documents générés. [#718]
- **Interface utilisateur :**
    - Ajout de titres de colonnes fixes (sticky headers) sur les listes de projets, simulations et programmations pour faciliter la navigation. [#704]
    - Correction de l'ouverture du dropdown de statut sans casser les colonnes stickies. [#711]
    - Autorisation des tabulations dans les arrêtés/lettres de notification. [#705]

### Évolutions techniques
- **Synchronisation DS :**
    - Implémentation d'un verrou (Redis lock) pour empêcher les synchronisations de dossiers DS concurrentes, améliorant ainsi la robustesse du système. [#740]
    - Amélioration de la gestion des erreurs lors de la sauvegarde des curseurs de pagination lors de la synchronisation avec DN. [#724]
    - Refactorisation du code de synchronisation DS pour améliorer la lisibilité et la maintenabilité.
- **Architecture :**
    - Découpage du document GraphQL monolithique en plusieurs fichiers plus petits et plus gérables. [#721]
    - Refactorisation de la gestion des managers `Active*Manager` pour utiliser les méthodes `queryset .active()`.
    - Refactorisation de la logique de mise à jour des montants pour centraliser le code et améliorer la cohérence.
- **Performance :**
    - Évaluation paresseuse des choix dans les FilterSet pour améliorer les performances. [#703]
    - Optimisation de la génération d'arrêtés/lettres en masse. [#714]
- **Divers :**
    - Mise à jour des dépendances vulnérables signalées par Dependabot. [#710]
    - Ajout de tests pour éviter les tests flaky. [#738]
    - Cache-busting des fichiers JS de l'importmap pour forcer la mise à jour des ressources en cache. [#745]
    - Suppression des rafraîchissements DS bloquants à l'ouverture des modales. [#743]
    - Correction d'une erreur de manifest staticfiles sur l'importmap. [#746]

### Autres changements
- Ajout d'un fichier `AGENTS.md` pour fournir des instructions aux agents de code. [#715, #722]
- Documentation sur l'utilisation des branches hotfix pour le déploiement par tag.
- Correction de la perte du curseur des dossiers supprimés sur les pages vides. [#742]
- Correction de l'affichage des largeurs de tableaux TipTap dans l'export PDF. [#734]
- Amélioration de la FAQ. [#732]
- Suppression des pages d'administration de l'application. [#726]
- Correction d'un bug empêchant les utilisateurs DN de mettre à jour leur adresse email. [#700]
- Correction d'un bug lié à l'utilisation de l'éditeur TipTap et à la gestion des tableaux. [#733]
- Correction d'un bug lié à l'affichage des statuts dans l'interface d'administration.
- Correction de l'utilisation de caractères invalides dans les noms de fichiers générés.
- Ajout de logging structuré et d'identifiants de requête sur le proxy DS.
- Amélioration de la gestion des actions significatives sur les projets.
- Ajout de la possibilité de stocker l'assiette lors du changement depuis DN.
- Ajout de l'enveloppe et suppression temporaire des statuts.
- Ajout d'un identifiant de formulaire.
- Rendre l'onglet historique accessible depuis toutes les applications.
- Mise à jour des dotations ajoutées/supprimées.
- Renommage du champ `montant` en `euro_field_value` et nettoyage du code.
- Centralisation de la mise à jour du montant dans la transition et mise à jour de l'interface utilisateur.

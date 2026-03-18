## Changelog : mon-service-securise (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la gestion des risques, avec l'introduction d'une nouvelle version (V2) des risques, incluant la gestion de leur activation/désactivation, l'ajout de propriétés comme la vraisemblance et la gravité, et une refonte du moteur de calcul des risques. Des améliorations ont également été apportées à l'interface utilisateur pour afficher et manipuler ces nouveaux risques. Enfin, plusieurs suppressions de code obsolète liées à l'ancien système d'authentification ont été effectuées.

### Évolutions fonctionnelles

*   Possibilité de désactiver un risque directement depuis le tableau des risques.
*   Ajout d'une colonne de vraisemblance et de gravité dans le tableau des risques.
*   Affichage des risques désactivés dans les matrices.
*   Ajout d'une propriété "commentaire" aux risques V2.
*   Mise à jour des données d'un risque V2 via le dépôt de données.
*   Affichage de la thématique et des porteurs singuliers dans le tiroir des mesures et dans le tableau des mesures.
*   Ajout de la transcription dans le tampon d'homologation.
*   Amélioration de l'affichage des filtres dans le tableau des données brutes (TDB).
*   Possibilité de supprimer les brouillons de service depuis le tiroir.
*   Amélioration de la sélection des services et des brouillons.

### Évolutions techniques

*   Migration vers Svelte 5.
*   Refonte du moteur de calcul des risques pour utiliser la version V2 des risques.
*   Conversion de nombreux modèles de données et adaptateurs en TypeScript pour une meilleure typage et maintenabilité.
*   Suppression du code lié à l'ancien système d'authentification MSS et à la gestion des mots de passe.
*   Mise à jour de plusieurs dépendances (Express, knex, jsonwebtoken, axios, etc.).
*   Amélioration de la gestion des erreurs et ajout de tests.
*   Refactoring du code pour améliorer la lisibilité et la maintenabilité.
*   Ajout de `svelte-check` dans la CI pour garantir la qualité du code Svelte.
*   Utilisation d'Express 5.

### Autres changements

*   Ajout de métadonnées.
*   Suppression du composant et de la page "Ui Kit".
*   Ajout d'un script pour générer les données de référence des vraisemblances de risques.
*   Correction de plusieurs erreurs et warnings dans le code.
*   Amélioration de la configuration et des processus de déploiement.
*   Ajout de la ConsoleBrevo pour migrer l'attribut SMS.
*   Mise à jour de l'UI Kit.
*   Correction de l'avance rapide sur décrireV2.
*   Correction de l'application des filtres et des onglets aux brouillons.
*   Correction de la mise en avant du bouton de création de service.
*   Correction de l'imbrication de balises `<a>`.
*   Correction des erreurs liées à `svelte-check`.
*   Correction des propriétés CSS.
*   Correction du typage.
*   Correction des erreurs suite à la migration automatisée.
*   Correction des select et des champs texte.
*   Correction des erreurs de `runtime`.
*   Correction du fichier de sortie des styles compilés.
*   Correction des warnings de `svelte-check`.
*   Correction des erreurs de typage.
*   Correction de l'affichage des filtres du TDB.
*   Correction de l'affichage des filtres du TDB.
*   Correction des erreurs liées à `svelte-check`.
*   Correction des erreurs liées à `svelte-check`.
*   Correction de l'imbrication de balises `<a>`.
*   Correction de l'intitulé du risque.
*   Correction de la suppression des mesures.
*   Correction de l'affichage du contenu.
*   Correction de la limite de caractères pour l'intitulé du risque.
*   Correction de l'erreur de suppression.
*   Correction de l'erreur de validation de payload.
*   Correction du calcul de vraisemblance.
*   Correction de l'utilisation du modèle `RisqueV2` dans le moteur de risque.
*   Correction de l'intégration des données de référence des intitulés de risques.
*   Correction de l'utilisation de la configuration de référence pour les intitulés de risques.
*   Correction de la génération de l'intitulé d'un risque.
*   Correction de l'utilisation de la vraisemblance.
*   Correction de l'utilisation des niveaux de sécurité.
*   Correction de l'ajout des risques avec gravité dans le moteur de risque.
*   Correction de l'utilisation des opérateurs "+".
*   Correction de la sécurité des mesures personnalisées.
*   Correction de l'ajout du prédicat "siPasTout".
*   Correction de l'ajout des configurations pour le calcul des vraisemblances.
*   Correction de l'autorisation du groupe de mesure 'g'.
*   Correction de la gestion des erreurs qui ne proviennent pas d'axios.
*   Correction de la gestion des erreurs.
*   Correction de l'utilisation du modèle `RisqueV2` dans le moteur de risque.
*   Correction de l'intégration des données de référence des intitulés de risques.
*   Correction de l'utilisation de la configuration de référence pour les intitulés de risques.
*   Correction de la génération de l'intitulé d'un risque.
*   Correction de l'utilisation de la vraisemblance.
*   Correction de l'utilisation des niveaux de sécurité.
*   Correction de l'ajout des risques avec gravité dans le moteur de risque.
*   Correction de l'utilisation des opérateurs "+".
*   Correction de la sécurité des mesures personnalisées.
*   Correction de l'ajout du prédicat "siPasTout".
*   Correction de l'ajout des configurations pour le calcul des vraisemblances.
*   Correction de l'autorisation du groupe de mesure 'g'.
*   Correction de la gestion des erreurs qui ne proviennent pas d'axios.
*   Correction de la gestion des erreurs.
*   Correction de l'utilisation du modèle `RisqueV2` dans le moteur de risque.
*   Correction de l'intégration des données de référence des intitulés de risques.
*   Correction de l'utilisation de la configuration de référence pour les intitulés de risques.
*   Correction de la génération de l'intitulé d'un risque.
*   Correction de l'utilisation de la vraisemblance.
*   Correction de l'utilisation des niveaux de sécurité.
*   Correction de l'ajout des risques avec gravité dans le moteur de risque.
*   Correction de l'utilisation des opérateurs "+".

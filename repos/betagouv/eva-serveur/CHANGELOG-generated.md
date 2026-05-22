## Changelog : eva-serveur (30 derniers jours, au 2026-05-21)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment avec l'adoption du Design System de l'État (DSFR) pour une meilleure cohérence visuelle et accessibilité. Des corrections de bugs et des optimisations de sécurité ont également été implémentées. Des fonctionnalités spécifiques aux Opérateurs de Compétences (OPCO) ont été ajoutées, incluant un tableau de bord dédié et une gestion des accès restreinte.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord dédié aux Opérateurs de Compétences avec intégration des statistiques Metabase.
- Possibilité pour les comptes OPCO d'accéder à leur dashboard.
- Amélioration de la gestion des invitations pour les structures administratives.
- Affichage du SIRET pour toutes les structures et ajout d'un filtre de recherche par SIRET.
- Possibilité de fermer les modales en cliquant sur le fond.
- Correction du double rendu d'erreur dans le contrôleur des nouveaux comptes.
- Ajout d'une méthode pour calculer la complétude des évaluations EVAPRO.
- Permet de générer les PDF en environnement de développement.
- Ajout d'une gestion des réponses "Je ne sais pas" pour les questions d'impacts et risques.
- Les utilisateurs OPCO ont désormais un accès restreint à la navigation d'EVA.
- Ajout d'une page pour lister les structures Opérateurs de Compétences.
- Correction de l'affichage des évaluations incomplètes pour EvaPro.
- Ajout d'une validation sur l'extension des fichiers audio dans le modèle Transcription.

### Évolutions techniques
- Migration vers le Design System de l'État (DSFR) pour de nombreux composants de l'interface utilisateur (tableaux, boutons, formulaires, etc.).
- Refactoring de la logique de formatage du SIRET et ajout de tests.
- Suppression de code obsolète (pages, actions, dépendances inutiles).
- Mise à jour des dépendances : JWT, Nokogiri, ERB, PostCSS, Devise, Fast-URI.
- Correction d'une vulnérabilité d'injection SQL dans CollectionsEvenementsController.
- Correction d'une faille de sécurité sur TarteauCitronJS.
- Suppression des utilities Bootstrap.
- Mise à jour de Ruby et Nodejs.
- Suppression des tests JS sur les actualités.
- Suppression des fichiers .pgsql inutiles.
- Amélioration de la performance en corrigeant un N+1 sur la page des actualités.
- Refactorisation de la gestion des modales.
- Suppression de la librairie geocoder.

### Autres changements
- Documentation de la variable d'environnement du tableau Metabase des OPCO.
- Alignement des breakpoints CSS sur ceux du DSFR.
- Suppression de classes CSS inutilisées.
- Suppression de commentaires inutiles.
- Ajout de commentaires et de documentation pour clarifier le code.
- Correction de problèmes de style et d'affichage sur différentes pages (actualités, comptes, structures, etc.).
- Suppression de certains fichiers de configuration inutiles.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'un composant "Incontournables" pour la vue PDF.
- Suppression du numéro de téléphone de Gaelle.
- Ajout de la possibilité de vider les comptes créés en démo, même invités.
- Correction de l'affichage des actualités.
- Correction de l'intégration du JS du DSFR.
- Correction du menu du DSFR.
- Ajout de logs pour le débogage.
- Suppression de l'étape de recherche de structure.
- Suppression du bouton d'ajout de structure.
- Suppression de la page admin/recherche_structure.
- Suppression de la page admin/sign_up.
- Suppression de la page nouvelle_structure.
- Suppression de la possibilité de créer un compte avec l'ID de structure.
- Suppression de l'action rejoindre_structure.
- Suppression du bouton copier/coller dans la modal invitation des structures Opco et Administrative.
- Suppression des informations concernant la géoloc.
- Suppression du code mort concernant le rattachement des structures administratives à un OPCO.
- Correction de l'affichage de l'index compte sur EvaPro.
- Correction de l'affichage de l'index des évaluations pour EvaPro.
- Correction du focus des boutons DSFR sur Firefox.
- Ajout d'un padding sur le tableau des évaluations Eva sur mobile.
- Correction de l'intégration des actualités.
- Correction de l'affichage de la page Ma structure sur mobile.
- Correction de la modale d'invitation.
- Correction du visuel des actualités.
- Correction de la page aide sur mobile.
- Correction de la page mon compte sur mobile.
- Correction de la page détail d'un bénéficiaire sur mobile.
- Correction du rendu de l'index des actualités.
- Correction du rendu de l'index des comptes sur EvaPro.
- Ajout d'un placeholder au select Role dans la modal d'invitation.
- Ajout du logo Evapro dans la démonstration.
- Ajoute le padding bottom pour les labels des forms.
- Corrige la redirection pour les comptes ProConnect sans structure.
- Corrige la partie mobile du contact opco dans evalutaion.
- Corrige le bug des accès.
- Ajoute la fonctionnalité d'invitation pour les structures administratives.
- Corrige le visuel des actualités.
- Corrige l'affichage des actualités.
- Corrige l'index des comptes sur EvaPro.
- Corrige la modale d'invitation.
- Corrige le rendu de l'index des actualités.
- Corrige l'index des comptes sur EvaPro.
- Corrige la page aide sur mobile.
- Corrige la page mon compte sur mobile.
- Corrige la page détail d'un bénéficiaire sur mobile.
- Corrige le rendu de l'index des actualités.
- Corrige l'index des comptes sur EvaPro.
- Ajout d'un placeholder au select Role dans la modal d'invitation.
- Ajout du logo Evapro dans la démonstration.
- Ajoute le padding bottom pour les labels des forms.
- Corrige la redirection pour les comptes ProConnect sans structure.
- Corrige la partie mobile du contact opco dans evalutaion.
- Corrige le bug des accès.
- Ajoute la fonctionnalité d'invitation pour les structures administratives.

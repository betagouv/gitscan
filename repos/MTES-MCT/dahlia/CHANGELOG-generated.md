## Changelog : dahlia (30 derniers jours, au 07 octobre 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour faciliter la gestion quotidienne des dossiers (ajout de mots-clés, synchronisation automatique, exports enrichis) et d'un renforcement important de la sécurité et de la traçabilité des actions effectuées par les administrateurs.

### Évolutions fonctionnelles
- **Gestion des dossiers** : 
    - Ajout de la fonctionnalité de mots-clés (tags) pour les dossiers [#137].
    - Possibilité de préciser les dossiers à enrichir via une nouvelle option [#144].
    - Synchronisation automatique des dossiers lors de chaque accès [#145] et possibilité de synchroniser l'ensemble des dossiers d'une juridiction spécifique [#159].
    - Utilisation du nom du dossier pour le nommage des fichiers ZIP téléchargés [#143].
- **Classification et Export** : 
    - Exportation des résultats de la classification [#129] incluant désormais le champ "statut" [#153].
    - Mise en place de nouvelles règles de classification [#170].
- **Expérience utilisateur (UX)** : 
    - Clarification de l'interface via le renommage de certains termes (ex: "Tags" devient "Mots clés") [#146].
    - Amélioration de la gestion des erreurs (messages moins verbeux [#173] et masquage des erreurs techniques Prisma [#157]).
    - Gestion de la déconnexion avec redirection automatique vers ProConnect [#169].
    - Mise à disposition des pages de mentions légales pour tous les utilisateurs [#155] et les administrateurs [#151].
- **Corrections** : 
    - Isolation de la suppression des dossiers pour éviter tout impact sur les autres juridictions [#161].
    - Identification et distinction des décisions de la COMED [#156].

### Évolutions techniques
- **Sécurité et Traçabilité** : 
    - Mise en place de logs d'audit pour tracer les refus d'accès [#174] et les actions réalisées dans l'interface d'administration [#158].
    - Renforcement de la sécurité via l'ajout de headers de sécurité [#131] et la mise à jour de librairies critiques pour corriger des alertes de sécurité [#167, #166].
    - Amélioration du contrôle de session pour les droits administrateur [#171].
- **Architecture et Performance** : 
    - Passage de la synchronisation des dossiers en mode asynchrone pour améliorer la réactivité [#152].
    - Modification de la structure de la clé primaire pour inclure le `JurisdictionCode` sur les éléments dépendants d'un dossier [#175].
    - Assouplissement des règles de sécurité d'affichage (x-frame) pour permettre la consultation des pièces jointes [#142].
    - Gestion d'instances distinctes pour certains processus métier [#160].

## Changelog : pitchou (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des données, la migration vers de nouvelles infrastructures de stockage, et l'ajout de nouvelles fonctionnalités pour faciliter le travail des agents de l'administration. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger les événements utilisateurs pour les statistiques AARRI. [#591]
- Ajout d'une page d'erreur 404 personnalisée pour une meilleure expérience utilisateur. [#596]
- Amélioration de la section évolution des indicateurs AARRI dans les statistiques. [#597]
- Ajout d'un bouton "Retour" sur la page des dossiers. [#609]
- Ajout d'un fil d'Ariane pour faciliter la navigation dans la documentation. [#610]
- Possibilité d'éditer les dates de consultation du public dans l'onglet instruction. [#600]
- Possibilité d'éditer le champ "enjeux" dans l'instruction. [#604]
- Ajout de la possibilité d'ajouter des pièces jointes aux seeds. [#614]
- Ajout de nouveaux fichiers de saisine CSRPN de la DREAL ARA et un nouveau mail de saisine au CNPN.
- Ajout de la possibilité d'autoriser les domaines ext.beta.gouv.fr et loir-et-cher.gouv.fr pour la connexion. [#601]
- Ajout de l'espèce *Cosentinia vellea* à la liste des espèces protégées du CNPN. [#66dcc9c]
- Affichage d'un message d'erreur si le domaine utilisé pour la connexion n'est pas autorisé. [#602]
- Ajout de dossiers D10 et D11 aux seeds. [#623]

### Évolutions techniques
- Migration des fichiers vers Outscale Object Storage pour une meilleure scalabilité et fiabilité. [#573]
- Migration du frontend de Svelte vers Typescript. [#568, #567]
- Refactorisation du dépôt en monorepo pour une meilleure organisation du code. [#595, #593]
- Correction du fuseau horaire des dates. [#612]
- Correction du chemin du schéma DS pour le worker. [#603]
- Suppression des liens vers la démarche numérique dans les dossiers/avis d'expert. [#5554cde]
- Suppression de la synchronisation des "enjeux politique et écologique" (annotation privée) depuis la démarche numérique. [#605]
- Suppression de la date d'envoi de la dernière contribution dans l'historique. [#615]
- Suppression de la personne associée à un dossier si elle n'y a plus accès. [#625]
- Mise à jour du DPO dans la documentation sur les données personnelles. [#624]

### Autres changements
- Mise à jour des modèles pour la génération de documents. [#5f8e0f5]
- Ajout de seeds plus réalistes pour les dossiers. [#608]
- Correction du format du fichier CSV pour les événements métriques AARRI. [#585]
- Ajout de la matrice d'impact à la page des statistiques. [#599]
- Correction de bugs liés à la synchronisation des données en local.
- Correction d'erreurs 500 lors du téléchargement de fichiers. [#587]
- Correction de problèmes d'affichage du fichier espèces impactées après la migration vers l'object storage. [#590]
- Correction de problèmes de réinitialisation de l'état "vu" des notifications lors de la synchronisation. [#592]
- Ajout de domaines autorisés pour la connexion. [#579]
- Suppression de décisions administratives en double lors de la synchronisation. [#584]
- Amélioration de la conformité du header et du footer avec les standards DSFR. [#583]
- Fusion de la page AARRI dans la page des statistiques. [#582]
- Ajout de liens vers les pages de statistiques, de budget et du bouton de thème dans le footer. [#581]
- Ajout de documentation sur le suivi des événements utilisateurs. [#586]
